function carregar(){

    let msg = window.document.querySelector('div#msg')
    let foto = window.document.querySelector('img#foto')
    let data = new Date()
    let hora = data.getHours()
    //let hora =
    msg.innerHTML = `Agora são ${hora} horas`

    if (hora >= 0 && hora < 12){
        foto.src = 'imagens/manha.png'
        document.body.style.background = '#f3f59a'
    }else if (hora >= 12 && hora < 18){
        foto.src = 'imagens/tarde.png'
        document.body.style.background = '#e3a344'
    }else{
        foto.src = 'imagens/noite.png'
        document.body.style.background = '#4c5465'
    }

}
