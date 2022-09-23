"""_summary_"""
import sys
from loguru import logger


def fltro_teste(dados):
    """_summary_"""
    if 'senha' in dados['message']:
        return False
    return True


logger.remove()

logger.level("FINALIZADO", no=23, color="<yellow>", icon="👍")

logger.add(
    sys.stderr,
    format='<level>{level}</level> :: <g>{time:YYYY-MM-DD HH:mm:ss}</g> :: <level>{message}</level> :: <ly>{file}-{line}</ly>',
    filter=fltro_teste
)

logger.add(
    'logs/teste.log',
    format='{level} :: {time:YYYY-MM-DD HH:mm:ss} :: {message} :: {file}-{line}',
    filter=fltro_teste,
    level='INFO',
    retention="20 days",
    diagnose=True
)

logger.add(
    'logs/teste_sucesso.log',
    format='{level.icon} {level} :: {time:YYYY-MM-DD HH:mm:ss} :: {message} :: {file}-{line}',
    level='FINALIZADO',
    diagnose=False,
    filter= lambda record: record['extra']['task'] == 'sucesso'
)

sucesso = logger.bind(task='sucesso')

logger.debug('Debug')
logger.info('Info')
logger.warning('Warn')
logger.error('Erro')
logger.critical('senha')
sucesso.log("FINALIZADO", "Finalozado log level customizado")

def func(num_um: int, num_dois: int) ->int:
    """_summary_"""
    return num_um / num_dois

def nested(num_zero: int)-> None:
    """_summary_"""
    try:
        func(5, num_zero)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)