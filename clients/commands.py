import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manages the client lifecycle"""
    pass

@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-n', '--company',
              type=str,
              prompt=True,
              help='The company name')
@click.option('-n', '--email',
              type=str,
              prompt=True,
              help='The email name')
@click.option('-n', '--position',
              type=str,
              prompt=True,
              help='The position name')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)

@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass

@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""
    pass

@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass

all = clients
