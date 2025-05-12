const students = {
    'name': 'Krishna Kumar Mandal',
    'roll': 11,
    'address': 'Biratnagar',
    'greet': function greet(name) {
        return `Hello, ${name}`
    }
}

// students['name'] = 'John Adams'
// console.log(students.name)
// console.log(students['roll'])
// console.log(students)

// delete students['name']
// console.log(students)

// ----------------------------------

console.log(students.greet(students.name))