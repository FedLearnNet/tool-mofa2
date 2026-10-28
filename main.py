from pyfedappwrap.engine.runtime import FedDBEngine

from app import MofaExplorationApp

engine = FedDBEngine()
engine.register(MofaExplorationApp())

if __name__ == '__main__':
    engine.start()
    engine.wait_until_stop()
