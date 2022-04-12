function gerar() {
    // variaeis com os elementos html:
    var numero = document.querySelector('input#number')
    var select = document.querySelector('select#select')

    // limpar o select:
    select.innerHTML = ''

    for (var c = 1; c < 11; c++){
        var res = Number(numero.value) * c
        select.innerHTML += `<option>${Number(numero.value)} x ${c} = ${res} </option>`

    }
}