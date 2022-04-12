function verificar() {
    
    var data = new Date()
    var ano = data.getFullYear()
    var fano = window.document.getElementById("txtano")
    var res = document.querySelector("div#res")

    if(fano.value.length == 0 || fano.value > ano) {

        window.alert("ERRO: dados inválidos")
    } else {

        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)

        var genero = ''

        var img = document.createElement('img')
        img.setAttribute('id', 'foto')


        if (fsex[0].checked) {
            genero = 'homem'
            if (idade >= 0 && idade <= 10) {
                //criança
                img.setAttribute('src', 'imagens/foto-bebe-m.png')
            } else if (idade <= 21) {
                //jovem
                img.setAttribute('src', 'imagens/foto-jovem-m.png')
            } else if (idade <= 50) {
                //adulto
                img.setAttribute('src', 'imagens/foto-adulto-m.png')
            } else {
                //idoso
                img.setAttribute('src', 'imagens/foto-idoso-m.png')
            }

        } else {
            genero = 'mulher'
            if (idade >= 0 && idade <= 10) {
                //crianca
                img.setAttribute('src', 'imagens/foto-bebe-f.png')

            } else if (idade <= 21) {
                //jovem
                img.setAttribute('src', 'imagens/foto-jovem-f.png')

            } else if (idade <= 50){
                //adulto
                img.setAttribute('src', 'imagens/foto-adulto-f.png')

            } else {
                //idoso
                img.setAttribute('src', 'imagens/foto-idoso-f.png')

            }
        }

        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos`
        res.appendChild(img)
    }

}