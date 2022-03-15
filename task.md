{% include navigation.html %}
## Create Task Plan
#### Idea: How stressed are you? quiz

The Stress Quiz page is the practice create task. 
It's main goal is to quiz users on how stressed the students are so that users can remember how much pressure they are going through in their school life.

This page will be integrated into our website as a PBL feature for now. The users will see a page where they can answer multiple-choice questions and receive their score upon submitting the quiz.
<hr>

* **Program Purpose:** Create a page that quizzes users based on their answers to the questions related to stress given

* **Input:** Selecting answers for questions

* **Output:** Displays user score upon submission

* **Lists:** Stores questions and answers in a list, then displays them later.

* **Procedure:** Once the user fills out all of the questions, the website will add +1 to the user's score if the answer is correct, then display it.

* **Parameters:** Score after user submits quiz

* **Sequencing:** User input in the quiz, Adds to score in case of a correct answer, Return percentage of how stresses the user is  

* **Selection:** Adds to score in case of a correct answer

* **Iteration:** Program loops for every question

### Code Snippet #1:

function loadPreviousQuestion() {
            currentQuestion--;
            score.pop();
            generateQuestions(currentQuestion);
        }

        function restartQuiz(e) {
            if(e.target.matches('button')) {
                currentQuestion = 0;
                score = [];
                location.reload();
            }

        }


        generateQuestions(currentQuestion);
        nextButton.addEventListener('click', loadNextQuestion);
        previousButton.addEventListener('click',loadPreviousQuestion);
        result.addEventListener('click',restartQuiz);

### Code Snippet #2:

   let currentQuestion = 0;
        let score = [];
        let selectedAnswersData = [];
        const totalQuestions =questions.length;

        const container = document.querySelector('.quiz-container');
        const questionEl = document.querySelector('.question');
        const option1 = document.querySelector('.option1');
        const option2 = document.querySelector('.option2');
        const option3 = document.querySelector('.option3');
        const nextButton = document.querySelector('.next');
        const previousButton = document.querySelector('.previous');
        const restartButton = document.querySelector('.restart');
        const result = document.querySelector('.result');

        function generateQuestions (index) {

            const question = questions[index];
            const option1Total = questions[index].answer1Total;
            const option2Total = questions[index].answer2Total;
            const option3Total = questions[index].answer3Total;

            questionEl.innerHTML = `${index + 1}. ${question.question}`
            option1.setAttribute('data-total', `${option1Total}`);
            option2.setAttribute('data-total', `${option2Total}`);
            option3.setAttribute('data-total', `${option3Total}`);
            option1.innerHTML = `${question.answer1}`
            option2.innerHTML = `${question.answer2}`
            option3.innerHTML = `${question.answer3}`
        }
