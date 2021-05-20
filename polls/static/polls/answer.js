document.addEventListener('DOMContentLoaded', function() {
    const questions = Array.from(document.querySelectorAll('.question-container'))
    var post_data = {}
    const finish_button = document.getElementById('finish-button')

    function hide_question(id) {
        for (let index = 0; index < questions.length; index++) {
            if (questions[index].id == id) {
                questions[index].classList.remove('fade-in')
                questions[index].classList.add('fade-out')
                
                setTimeout(function () {
                    questions[index].classList.add('d-none')

                    try {
                        questions[index+1].classList.remove('d-none')
                        questions[index+1].classList.add('fade-in')
                    } catch (error) {
                        document.getElementById('finish-div').classList.remove('d-none')
                        document.getElementById('finish-div').classList.add('fade-in')
                    }
                }, 1000)
            }
        }
    }

    questions.forEach(question => {
        question.querySelectorAll('button').forEach(btn => {
            btn.onclick = () => {
                post_data[question.id] = btn.getAttribute('data-answer')
                hide_question(question.id)
            }
        })
    })

    finish_button.onclick = () => {
        const form = finish_button.parentElement

        for (const question of Object.keys(post_data)) {
            const value = post_data[question]
            var input = document.createElement('input')

            input.setAttribute('type', 'hidden')
            input.setAttribute('name', question)
            input.setAttribute('value', value)

            form.appendChild(input)
        }

        form.submit()
    }
})