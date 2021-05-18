document.addEventListener('DOMContentLoaded', function () {
    const question_mold = document.getElementById('question-mold')
    const form = document.querySelector('#create-form')
    
    function add_question() {
        let new_question = question_mold.cloneNode(true)
        new_question.classList.replace('d-none', 'question')

        let last_question = Array.from(document.getElementsByClassName('question')).pop()
        let new_question_num = parseInt(last_question.id.charAt(last_question.id.length-1)) + 1

        new_question.id = `question-${new_question_num}`

        let question_inputs = Array.from(new_question.querySelectorAll('input'))

        question_inputs[0].setAttribute('name', `question_title_${new_question_num}`)
        question_inputs[1].setAttribute('name', `answer_${new_question_num}_1`)
        question_inputs[2].setAttribute('name', `answer_${new_question_num}_2`)
        question_inputs[3].setAttribute('name', `answer_${new_question_num}_3`)
        question_inputs[4].setAttribute('name', `answer_${new_question_num}_4`)

        form.insertBefore(new_question, document.getElementById('add-question').parentElement)
        document.getElementById('remove-question').disabled = false
    }

    function remove_last_question() {
        let questions = Array.from(document.getElementsByClassName('question'))
        questions.pop().remove()

        if (questions.length <= 1) {
            document.getElementById('remove-question').disabled = true
        }
    }

    document.getElementById('add-question').onclick = add_question
    document.getElementById('remove-question').onclick = remove_last_question

    document.getElementById('submit-button').onclick = () => question_mold.remove()
})