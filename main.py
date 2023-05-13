import argparse
import pandas as pd


def main(config_paths):
    dfs = []
    for config_path in config_paths:
        data = pd.read_csv(''.join(config_path))
        dfs.append(data)
        print('completed {}'.format(''.join(config_path)))

    concatinated_df = pd.concat(dfs, ignore_index=True)
    print(concatinated_df)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', type=list, nargs='+')
    parse_args = args.parse_args()
    main(config_paths=parse_args.config)
