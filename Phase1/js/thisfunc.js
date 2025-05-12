const students = {
    'name': 'Krishna Kumar Mandal',
    'roll': 11,
    'address': 'Biratnagar',
    // 'greet': function greet(name) {
    // return `Hello, ${name}`
    'greet': function greet() {
        return `Hello, ${this.name}. You live in ${this.address}`
    }
}

console.log(students.greet())