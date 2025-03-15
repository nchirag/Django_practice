from django.shortcuts import render,redirect

# Create your views here.
employees = [
    {'id': 1, 'name': 'Chirag', 'age': 23, 'contact': '12345', 'department': 'IT', 'status': 'Active'},
    {'id': 2, 'name': 'Sairaj', 'age': 22, 'contact': '67890', 'department': 'HR', 'status': 'Inactive'},
    {'id': 3, 'name': 'Kriti', 'age': 25, 'contact': '54321', 'department': 'Finance', 'status': 'Active'},
    {'id': 4, 'name': 'Ansel', 'age': 30, 'contact': '98765', 'department': 'Marketing', 'status': 'Active'}
]

def home(request):
    return render(request,'index.html')

def employee_list(request):
    return render(request,'employee_list.html',context = {'employees':employees})

def add_employee(request):
    if request.method == 'POST':
        new_employee = {
            'id': len(employees) + 1,
            'name': request.POST['name'],
            'age': request.POST['age'],
            'contact': request.POST['contact'],
            'department': request.POST['department'],
            'status': request.POST['status'],
        }
        employees.append(new_employee)
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'action': 'Add'})

def delete_employee(request, emp_id):
    global employees
    employees = [emp for emp in employees if emp['id'] != emp_id]
    return redirect('employee_list')

def edit_employee(request, emp_id):
    employee = next((emp for emp in employees if emp['id'] == emp_id), None)
    if not employee:
        return redirect('employee_list')
    
    if request.method == 'POST':
        employee['name'] = request.POST['name']
        employee['age'] = request.POST['age']
        employee['contact'] = request.POST['contact']
        employee['department'] = request.POST['department']
        employee['status'] = request.POST['status']
        return redirect('employee_list')
    
    return render(request, 'employee_form.html', {'action': 'Edit', 'employee': employee})


