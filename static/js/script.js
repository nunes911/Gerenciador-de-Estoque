function validarCadastro(){

    var nome = cadastro.nome.value;
    var registro = cadastro.cod_registro.value;
    var fabricante = cadastro.fabricante.value;
    var tipo = cadastro.tipo.value;

    if(nome == ""){
        cadastro.nome.focus();
        return false;
    }
    if(registro == ""){
        cadastro.cod_registro.focus();
        return false;
    }
    if(fabricante == ""){
        cadastro.fabricante.focus();
        return false;
    }
    if(tipo == ""){
        cadastro.tipo.focus();
        return false;
    }

    alert("Cadastro Realizado!")
}

function validarMovimento(){

    var movimentacao = estoque.movimentacao.value
    var quantidade = estoque.quantidade.value
    var data = estoque.data.value
    var local = estoque.local.value
    var registro = estoque.registro.value

    if (movimentacao == ""){
        estoque.movimentacao.focus()
        return false
    }
    if(registro == ""){
        estoque.registro.focus();
        return false;
    }
    if(quantidade == ""){
        estoque.quantidade.focus();
        return false;
    }
    if(data == ""){
        estoque.data.focus();
        return false;
    }
    
    if(local == ""){
        estoque.local.focus();
        return false;
    }
    
    alert("Movimentação Realizada!")
}

