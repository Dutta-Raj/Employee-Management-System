@echo off 
findstr /C:"150 characters or fewer" "C:\Users\KIIT\Desktop\employee_management_system\backend\templates\registration\register.html" 
if errorlevel 1 ( 
  echo Text not found 
) else ( 
  powershell -Command "(Get-Content 'C:\Users\KIIT\Desktop\employee_management_system\backend\templates\registration\register.html') -replace '150 characters or fewer', '8-10 characters or fewer' | Set-Content 'C:\Users\KIIT\Desktop\employee_management_system\backend\templates\registration\register.html'" 
  echo File updated successfully 
) 
