// Tem que fazer o jquery no html base
$(document).ready(function () {

    // URL base
    var baseUrl = 'http://localhost:8000'

    // Mapeando os elementos do html de acordo com $('name')
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');

    // Eventos ou ação (ao clicar)
    $(deleteBtn).on('click', function (e) { // Confirmação de exclusão de tarefa
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if(result) {
            window.location.href = delLink; // Muda de URL
        }
    });

    $(searchBtn).on('click', function(){
        searchForm.submit();
    });

    $(filter).change(function() {
        var filtro = $(this).val();
        console.log(filtro)
        window.location.href = baseUrl + '?filter=' + filtro; // Muda de URL
    });

});