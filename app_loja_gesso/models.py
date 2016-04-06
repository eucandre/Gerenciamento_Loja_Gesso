# coding=utf-8
from django.db import models

CONTA = ((u"Receber","R"), (u"Pagar", "P"))
PERIODO=((u"Constante diaria","Constante diaria"),(u"Constante semanal","Constante semanal"),(u"Constante mensal","Constante mensal"), (u"Esporatica", "Esporatica"))


class Fornecedor(models.Model):
    Nome = models.CharField(max_length=150, unique=True)
    Telefone = models.CharField(max_length=20)
    Telefone_conhecido = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    ativo = models.BooleanField(blank=True)
    observacoes_fornecedor = models.TextField()

    def __unicode__(self):
        return self.Nome

    class Meta:
        verbose_name_plural = "Fornecedor"

class Cliente(models.Model):
    Nome = models.CharField(max_length=150)
    Telefone = models.CharField(max_length=20)
    Telefone_conhecido = models.CharField(max_length=150)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    ativo = models.BooleanField(blank=True)
    observacoes_cliente = models.TextField()

    def __unicode__(self):
        return self.Nome

    class Meta:
        verbose_name_plural = "Cliente da loja"

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    codigo = models.CharField(max_length=150)
    quantidade = models.IntegerField()
    valor_unidade_compra = models.FloatField()
    valor_unidade_venda = models.FloatField()
    data_aquisicao = models.DateTimeField()
    fornecedor = models.ForeignKey(Fornecedor)
    observacao_produto = models.TextField()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Aquisição dos produtos"

class Vendas(models.Model):
    produto     = models.ForeignKey(Produto)
    cliente     = models.ForeignKey(Cliente)
    quantidade = models.FloatField()# quantidade do produto para a venda
    valor_para_venda = models.FloatField()
    data_da_venda = models.DateField()
    hora_da_venda = models.DateField()
    observacao_sobre_venda = models.TextField()

    def __unicode__(self):
        return self.observacao_sobre_venda


    class Meta:
        verbose_name_plural = "Vendas dos produtos"

class Manutencao_estoque(models.Model):
    data_estoque = models.DateField()
    quantidade_tipos_de_produtos = models.FloatField()#quantidade de tipos de produtos no estoque
    produtosEmEstoque = models.ManyToManyField(Produto) #quais os produtos no estoque ainda
    tipos_de_produtos_para_adiquirir = models.IntegerField()#Quantidade de produtos para adiquirir
    valor_aproximado_regularizar_estoque = models.FloatField()
    observacao_estoque = models.TextField()

    def __unicode__(self):
        return self.data_estoque

    class Meta:
        verbose_name_plural = "Manutenção do estoque"

class Contas(models.Model):
    nome_conta = models.CharField(max_length=150,)
    valor_conta = models.FloatField()
    data_vencimento = models.DateField()
    categoria = models.CharField(max_length=150,choices=CONTA)#se a conta eh para receber ou para pagar
    periodicidade = models.CharField(max_length=150,choices=PERIODO)#Com que frequencia a conta se repete
    observacao_conta = models.TextField()

    def __unicode__(self):
        return self.nome_conta

    class Meta:
        verbose_name_plural = "Contas da loja, recebimento e pagamento"

class ControleContas(models.Model):
    qual_conta = models.ForeignKey(Contas)#seleciona a conta
    pago = models.BooleanField(blank=True)# se desmarcada a conta não foi paga
    esta_fechada = models.BooleanField(blank=True)#se marcada a conta está encerrada
    data_pagamento = models.DateField()
    observacao_pagamento_contas = models.TextField()

    def __unicode__(self):
        return self.qual_conta

    class Meta:
        verbose_name_plural = "Controle das contas"

class EmCaixa(models.Model):
    """
        Esta classe contará todas as vendas e todas as compras efetuadas e fará subtrairá o total de vendas pelo total de compras.
        Contará com a data, atualizada autmomaticamente e a hora da última verificação, ou mudança.
    """
    objeto_Produtos_comprados = models.ForeignKey(Produto)
    objeto_Produtos_vendidos = models.ForeignKey(Vendas)

    def operacao(self):
        if (self.objeto_Produtos_comprados and self.objeto_Produtos_vendidos) == None:
            return 0
        elif (self.objeto_Produtos_comprados != None) and (self.objeto_Produtos_vendidos == None):
            return int(self.objeto_Produtos_comprados)
        elif (self.objeto_Produtos_comprados == None) and (self.objeto_Produtos_vendidos != None):
            return int(self.objeto_Produtos_vendidos)
        elif (self.objeto_Produtos_comprados != None) and (self.objeto_Produtos_vendidos != None):
            return int(self.objeto_Produtos_vendidos.valor_para_venda) - int(self.objeto_Produtos_comprados.valor_unidade_compra)
    data = models.DateField()
    hora = models.TimeField()
    valor = models.FloatField()

    def __unicode__(self):
        return self.valor
