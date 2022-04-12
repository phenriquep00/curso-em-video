function contar() {
    // Pegar os valores de dentro dos 3 inputs:
    var inicio = document.querySelector('input#inicio').value
    var fim = document.querySelector('input#fim').value
    var passo = document.querySelector('input#passo').value
    var res = document.querySelector('div#res')

    // Validar os dados:
    if (inicio == '') {
        window.alert('Nenhum valor de inicio para contagem. Considerando inicio = 0')
        inicio = 0
    } else if (Number(passo) <= 0) {
        window.alert('Valor de passo inválido. Considerando passo = 1')
        passo = 1
    }

    // Contagem:
    res.innerHTML = ''
    if (Number(inicio) <= Number(fim)) {
        for (var c = Number(inicio); c <= Number(fim); c += Number(passo)) {
            if (c >= Number(fim)) {
                res.innerHTML += `${c} &#127775`
            } else{
                res.innerHTML += `${c} &#127752 `
            }
        }    
    } else {
        for (var c = Number(inicio); c >= Number(fim); c -= Number(passo)) {
            if (c <= Number(fim)) {
                res.innerHTML += `${c} &#127775`
            } else {
                res.innerHTML += `${c} &#127752 `
            }           
        }
    }
}