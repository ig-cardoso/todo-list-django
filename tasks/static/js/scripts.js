// Tem que fazer o jquery no html base
$(document).ready(function () {

    // Mapeando os elementos do html
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    // Eventos (ao clicar)
    $(deleteBtn).on('click', function (e) { // Confirmação de exclusão de tarefa
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if (result) {
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function(){
        searchForm.submit();
    })

});