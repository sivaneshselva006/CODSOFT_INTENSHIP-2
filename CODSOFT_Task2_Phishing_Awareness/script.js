const quizForm = document.getElementById("quiz-form");
const result = document.getElementById("quiz-result");

quizForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const questions = [...document.querySelectorAll(".question")];
  let score = 0;
  let unanswered = 0;

  questions.forEach((question) => {
    const selected = question.querySelector("input:checked");
    if (!selected) {
      unanswered++;
      return;
    }
    if (selected.value === question.dataset.answer) score++;
  });

  result.classList.add("visible");
  if (unanswered > 0) {
    result.textContent = `You answered ${questions.length - unanswered} of ${questions.length} questions. Please answer all questions before submitting.`;
  } else {
    let message = "Review the safety tips and try again.";
    if (score === questions.length) message = "Excellent! You know how to spot common phishing risks.";
    else if (score >= 3) message = "Good work! Review the missed topic(s) to strengthen your awareness.";
    result.textContent = `Your score: ${score}/${questions.length}. ${message}`;
  }
  result.scrollIntoView({ behavior: "smooth", block: "nearest" });
});

quizForm.addEventListener("reset", function () {
  result.classList.remove("visible");
  result.textContent = "";
});
