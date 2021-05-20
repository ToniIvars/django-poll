document.addEventListener('DOMContentLoaded', function() {
    const share_btns = Array.from(document.getElementsByClassName('share-button'))
    const success_messages = Array.from(document.getElementsByClassName('success-message'))
    
    for (let index = 0; index < share_btns.length; index++) {
        const btn = share_btns[index]
        const message = success_messages[index]

        const id = btn.getAttribute('data-poll-id')
        const url = `${window.location.href.split('/').slice(0,3).join('/')}/answer/${id}`

        btn.onclick = () => {
            navigator.clipboard.writeText(url).then(function() {
                btn.classList.add('d-none')
                message.classList.remove('d-none')

            }, function(err) {
                console.error('Async: Could not copy text: ', err)
            })              
        }
    }
})