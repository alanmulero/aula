<?php
$conexao = mysqli_connect("localhost","root","","teste");
if (!$conexao) {
	die("Erro de conexão com DB");
	
}
$nome = $_POST['nome'];

$sql = "INSERT INTO tabela VALUES('$nome')";

$resultado = mysqli_query($conexao,$sql);

mysql_close($conexao);
?>