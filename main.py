import sys
import argparse

if __name__ == '__main__':
    """
    main.py 1 2 --log args.log 
    @since 2023年12月19日15:20:17
    """
    parser = argparse.ArgumentParser(description='sum the integers at the command line')
    parser.add_argument('integers', metavar='int', nargs='+', type=int, help='an integer to be summed')
    parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'), help='the file where the sum should be written')
    parser.add_argument("--data-provider", "-d", type=str, default="static")
    parser.add_argument("--input-data-path", "-n", type=str, default="data/input/coinbase-1h-btc-usd.csv")
    parser.add_argument("--reward-strategy", "-r", type=str, default="incremental-profit", dest="reward_strat")
    parser.add_argument("--pair", "-p", type=str, default="BTC/USD")
    parser.add_argument("--debug", "-D", action='store_false')
    parser.add_argument('--mini-batches', type=int, default=1, help='Mini batches', dest='n_minibatches')
    parser.add_argument('--train-split-percentage', type=float, default=0.8, help='Train set percentage')
    parser.add_argument('--verbose-model', type=int, default=1, help='Verbose model', dest='model_verbose')
    args = parser.parse_args()
    args.log.write('%s' % sum(args.integers))
    args.log.close()