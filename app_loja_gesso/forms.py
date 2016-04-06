from django import forms
from models import *

CONTA = ((u"Receber","R"), (u"Pagar", "P"))
PERIODO=((u"Constante diaria","Constante diaria"),(u"Constante semanal","Constante semanal"),(u"Constante mensal","Constante mensal"), (u"Esporatica", "Esporatica"))

class FormFornecedor(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = ["Nome", "Telefone", "Telefone_conhecido", "email", "rua", "bairro", "cidade", "ativo", "observacoes_fornecedor"]

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["Nome", "Telefone", "Telefone_conhecido", "email", "rua", "bairro", "cidade", "ativo", "observacoes_cliente"]

class FormProduto(forms.ModelForm):
    #nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = Produto
        fields =["nome", "codigo","quantidade","valor_unidade_compra","valor_unidade_venda","data_aquisicao","observacao_produto"]

class FormVendas(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ["produto", "cliente", "quantidade", "valor_para_venda", "data_da_venda", "hora_da_venda", "observacao_sobre_venda"]

class FormManutencao_estoque(forms.ModelForm):
    class Meta:
        model = Manutencao_estoque
        fields = ["data_estoque", "quantidade_tipos_de_produtos","produtosEmEstoque","tipos_de_produtos_para_adiquirir","valor_aproximado_regularizar_estoque","observacao_estoque"]

class FormContas(forms.ModelForm):
    class Meta:
        model = Contas
        fields = ["nome_conta","valor_conta","data_vencimento","categoria","periodicidade","observacao_conta"]

class FormControleContas(forms.ModelForm):
    class Meta:
        model = ControleContas
        fields = ["qual_conta","pago","esta_fechada","data_pagamento","observacao_pagamento_contas"]

class FormEmcaixa(forms.ModelForm):
    obj = EmCaixa()
    valor = forms.FloatField(initial=obj.operacao)
    class Meta:
        model = EmCaixa
        fields = ["data", "hora", "valor"]