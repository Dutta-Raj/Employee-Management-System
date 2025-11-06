const express = require('express');
const { Client } = require('pg');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;
app.use(express.json());

const client = new Client({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

// Connect to database
client.connect()
  .then(() => console.log('✅ Connected to PostgreSQL Database'))
  .catch(err => console.error('❌ Connection error:', err));

// Create employees table
client.query(`
  CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT NOW()
  )
`).then(() => console.log('✅ Employees table ready'))
  .catch(err => console.error('❌ Table creation error:', err));

// Routes
app.get('/', (req, res) => {
  res.send('🚀 Employee Management System is running!');
});

// Get all employees
app.get('/employees', async (req, res) => {
  try {
    const result = await client.query('SELECT * FROM employees ORDER BY id');
    res.json({
      success: true,
      data: result.rows,
      count: result.rowCount
    });
  } catch (err) {
    res.status(500).json({ 
      success: false,
      error: err.message 
    });
  }
});

// Add new employee
app.post('/employees', async (req, res) => {
  try {
    const { name, email, department, salary } = req.body;
    
    if (!name || !email) {
      return res.status(400).json({
        success: false,
        error: 'Name and email are required'
      });
    }

    const result = await client.query(
      'INSERT INTO employees (name, email, department, salary) VALUES ($1, $2, $3, $4) RETURNING *',
      [name, email, department, salary]
    );
    
    res.status(201).json({
      success: true,
      data: result.rows[0],
      message: 'Employee added successfully'
    });
  } catch (err) {
    res.status(500).json({ 
      success: false,
      error: err.message 
    });
  }
});

// Get employee by ID
app.get('/employees/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await client.query('SELECT * FROM employees WHERE id = $1', [id]);
    
    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        error: 'Employee not found'
      });
    }
    
    res.json({
      success: true,
      data: result.rows[0]
    });
  } catch (err) {
    res.status(500).json({ 
      success: false,
      error: err.message 
    });
  }
});

// Update employee
app.put('/employees/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { name, email, department, salary } = req.body;
    
    const result = await client.query(
      'UPDATE employees SET name = $1, email = $2, department = $3, salary = $4 WHERE id = $5 RETURNING *',
      [name, email, department, salary, id]
    );
    
    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        error: 'Employee not found'
      });
    }
    
    res.json({
      success: true,
      data: result.rows[0],
      message: 'Employee updated successfully'
    });
  } catch (err) {
    res.status(500).json({ 
      success: false,
      error: err.message 
    });
  }
});

// Delete employee
app.delete('/employees/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await client.query('DELETE FROM employees WHERE id = $1 RETURNING *', [id]);
    
    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        error: 'Employee not found'
      });
    }
    
    res.json({
      success: true,
      message: 'Employee deleted successfully',
      data: result.rows[0]
    });
  } catch (err) {
    res.status(500).json({ 
      success: false,
      error: err.message 
    });
  }
});

// Start server
app.listen(port, () => {
  console.log('🚀 Server running on http://localhost:' + port);
});