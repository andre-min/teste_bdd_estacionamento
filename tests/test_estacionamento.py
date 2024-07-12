"""Controle de Estacionamento feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
from pytest import fixture
import pytest
from app.estacionamento import Estacionamento, Ticket
from datetime import datetime, timedelta
@fixture
def estacionamento():
    return Estacionamento()

@fixture
def ticket():
    return Ticket(placa='ABC-9999', modelo='Fiat')


@scenario('../features/estacionamento.feature', 'Emitir um ticket para entrada de veiculo')
def test_emitir_um_ticket_para_entrada_de_veiculo():
    """Emitir um ticket para entrada de veiculo."""


@given(parsers.parse('um veiculo entra no Estacionamento'))
def entrada_veiculo(estacionamento, ticket):
    """um veiculo entra no Estacionamento."""
    estacionamento.emitir_ticket(ticket)

@when(parsers.parse('o frentista emite um ticket para o veiculo'))
def emitir_ticket(estacionamento, ticket):
    """o frentista emite um ticket para o veiculo."""
    estacionamento.emitir_ticket(ticket)

@then(parsers.parse('o ticket contem informacoes corretas sobre a entrada do veiculo'))
def verificar_informcoes_ticket(ticket):
    """o ticket contem informacoes corretas sobre a entrada do veiculo."""
    assert ticket.entrada is not None
    assert ticket.placa == 'ABC-9999'
    assert ticket.modelo == 'Fiat'


@scenario('../features/estacionamento.feature', 'Calcular o valor devido para a saida de veiculo')
def test_calcular_o_valor_devido_para_a_saida_de_veiculo():
    """Calcular o valor devido para a saida de veiculo."""

@given('um veiculo esta estacionado ha 2 horas')
def estacionado_2horas(ticket):
    """um veiculo esta estacionado ha 2 horas."""
    ticket.entrada = datetime.now() - timedelta(hours=2)


@when('o cliente apresenta o ticket de entrada para a saida')
def saida_veiculo(estacionamento, ticket):
    """o cliente apresenta o ticket de entrada para a saida."""
    estacionamento.registrar_saida(ticket)




@then('o frentista calcula o valor devido corretamente')
def calcular_valor_estacionamento(estacionamento, ticket):
    """o frentista calcula o valor devido corretamente."""
    vlr_devido = estacionamento.calcular_valor_devido(ticket)
    assert vlr_devido == pytest.approx(15 + (1 * 5))




