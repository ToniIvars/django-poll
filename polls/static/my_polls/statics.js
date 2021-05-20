document.addEventListener('DOMContentLoaded', function () {
    function make_chart(canvas, labels, votes_data) {
        var ctx = canvas.getContext('2d')
        var myChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    fill: true,
                    data: votes_data,
                    backgroundColor: ['#ff6384', '#36a2eb', '#ffce56', '#12e678'],
                    hoverOffset: 4
                }]
            }
        })
    }

    const cards = Array.from(document.getElementsByClassName('poll-card'))

    cards.forEach(card => {
        let labels = []
        let votes_data = []
        let canvas = card.querySelector('canvas')

        Array.from(card.getElementsByTagName('p')).forEach(p => {
            labels.push(p.innerHTML)
            votes_data.push(p.getAttribute('data-votes'))
        })

        make_chart(canvas, labels, votes_data)
    })
})