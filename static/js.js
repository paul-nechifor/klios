$(function () {
    handleCheckForm();
    handleRateForm();
});

function handleCheckForm() {
    var form = $('#check-form');
    if (form.length === 0) {
        return;
    }
    var submit = form.find('button.submit');
    $('body').keypress(function (ev) {
        if (ev.which === 13) {
            ev.preventDefault();
            form.submit();
        }
    });
}

function handleRateForm() {
    var form = $('#rate-form');
    if (form.length === 0) {
        return;
    }
    var correct = form.find('.correct');
    var incorrect = form.find('.incorrect');
    var score = form.find('#id_score');
    var correctFunc = function () {
        score.val('1.0');
        form.submit();
    }
    var incorrectFunc = function () {
        score.val('0.0');
        form.submit();
    }
    correct.click(correctFunc);
    incorrect.click(correctFunc);
    $('body').keypress(function (ev) {
        if (ev.which === 49) {
            incorrectFunc();
        } else if (ev.which === 50) {
            correctFunc();
        }
    });
}
