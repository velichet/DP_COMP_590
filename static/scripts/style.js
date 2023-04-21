var input = document.getElementsByTagName('input')
for(let i = 0; i < input.length; i++) {
    input[i].classList.add('form-control')
}

var label = document.getElementsByTagName('label')
for(let i = 0; i < label.length; i++) {
    label[i].classList.add('form-label')
}