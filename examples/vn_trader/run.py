# flake8: noqa
from vnpy.app.algo_trading import AlgoTradingApp
from vnpy.app.csv_loader import CsvLoaderApp
from vnpy.app.cta_backtester import CtaBacktesterApp
from vnpy.app.cta_strategy import CtaStrategyApp
from vnpy.app.data_recorder import DataRecorderApp
# from vnpy.app.risk_manager import RiskManagerApp
from vnpy.app.script_trader import ScriptTraderApp
from vnpy.event import EventEngine
from vnpy.gateway.bitfinex import BitfinexGateway
from vnpy.gateway.bitmex import BitmexGateway
# from vnpy.gateway.onetoken import OnetokenGateway
# from vnpy.gateway.xtp import XtpGateway
# from vnpy.gateway.hbdm import HbdmGateway
# from vnpy.gateway.tap import TapGateway
# from vnpy.gateway.tora import ToraGateway
# from vnpy.gateway.alpaca import AlpacaGateway
# from vnpy.gateway.da import DaGateway
from vnpy.gateway.coinbase import CoinbaseGateway
from vnpy.gateway.huobi import HuobiGateway
# from vnpy.gateway.futu import FutuGateway
from vnpy.gateway.ib import IbGateway
# from vnpy.gateway.ctp import CtpGateway
# from vnpy.gateway.ctptest import CtptestGateway
# from vnpy.gateway.mini import MiniGateway
# from vnpy.gateway.sopt import SoptGateway
# from vnpy.gateway.minitest import MinitestGateway
# from vnpy.gateway.femas import FemasGateway
# from vnpy.gateway.tiger import TigerGateway
# from vnpy.gateway.oes import OesGateway
from vnpy.gateway.okex import OkexGateway
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp


def main():
    qapp = create_qapp()

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)

    # main_engine.add_gateway(BinanceGateway)
    # main_engine.add_gateway(CtpGateway)
    # main_engine.add_gateway(CtptestGateway)
    # main_engine.add_gateway(MiniGateway)
    # main_engine.add_gateway(SoptGateway)
    # main_engine.add_gateway(MinitestGateway)
    # main_engine.add_gateway(FemasGateway)
    main_engine.add_gateway(IbGateway)
    # main_engine.add_gateway(FutuGateway)
    main_engine.add_gateway(BitmexGateway)
    # main_engine.add_gateway(TigerGateway)
    # main_engine.add_gateway(OesGateway)
    main_engine.add_gateway(OkexGateway)
    main_engine.add_gateway(HuobiGateway)
    main_engine.add_gateway(BitfinexGateway)
    # main_engine.add_gateway(OnetokenGateway)
    # main_engine.add_gateway(OkexfGateway)
    # main_engine.add_gateway(HbdmGateway)
    # main_engine.add_gateway(XtpGateway)
    # main_engine.add_gateway(TapGateway)
    # main_engine.add_gateway(ToraGateway)
    # main_engine.add_gateway(AlpacaGateway)
    # main_engine.add_gateway(OkexsGateway)
    # main_engine.add_gateway(DaGateway)
    main_engine.add_gateway(CoinbaseGateway)

    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(CsvLoaderApp)
    main_engine.add_app(AlgoTradingApp)
    main_engine.add_app(DataRecorderApp)
    # main_engine.add_app(RiskManagerApp)
    main_engine.add_app(ScriptTraderApp)
    # main_engine.add_app(RpcServiceApp)
    # main_engine.add_app(SpreadTradingApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()