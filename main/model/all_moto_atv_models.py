from dataclasses import dataclass


@dataclass
class ICEItem:
    brand: str
    model: str
    type: str
    price: str
    url: str
    year: str
    location: str
    added_date: str
    sold_date: str


moto_atv_brand_model_dict = {
    'honda': {
        'crf': 'motocicleta',
        'cbr-250': 'motocicleta',
        'cbr250': 'motocicleta',
        'cbr-300': 'motocicleta',
        'cbr300': 'motocicleta',
        'cbr-500': 'motocicleta',
        'cbr500': 'motocicleta',
        'cbr-600-f': 'motocicleta',
        'cbr600-f': 'motocicleta',
        'cbr-650-f': 'motocicleta',
        'cbr650-f': 'motocicleta',
        'cbr-600-rr': 'motocicleta',
        'cbr600-rr': 'motocicleta',
        'cbr-1000-rr': 'motocicleta',
        'cbr1000-rr': 'motocicleta',
        'cb-500': 'motocicleta',
        'cb500': 'motocicleta',
        'cb600': 'motocicleta',
        'cb-600': 'motocicleta',
        'cb-1100': 'motocicleta',
        'cb1100': 'motocicleta',
        'cbf-1000': 'motocicleta',
        'cbf1000': 'motocicleta',
        'hornet': 'motocicleta',
        'nc700': 'motocicleta',
        'nc750': 'motocicleta',
        'transalp': 'motocicleta',
        'varadero': 'motocicleta',
        'vfr-750': 'motocicleta',
        'vfr-800': 'motocicleta',
        'vfr-1200': 'motocicleta',
        'trx': 'atv',
        'explorer': 'atv',
        'fourtrax': 'atv',
        'rubicon': 'atv'
    },
    'kawasaki': {
        'er6': 'motocicleta',
        'ninja-250': 'motocicleta',
        'ninja250': 'motocicleta',
        'ninja-600': 'motocicleta',
        'ninja600': 'motocicleta',
        'ninja-636': 'motocicleta',
        'ninja636': 'motocicleta',
        'klx': 'motocicleta',
        'kle': 'motocicleta',
        'klr': 'motocicleta',
        'kx-450': 'motocicleta',
        'kx450': 'motocicleta',
        'kxf-450': 'motocicleta',
        'kxf450': 'motocicleta',
        'z650': 'motocicleta',
        'z-650': 'motocicleta',
        'z750': 'motocicleta',
        'z-750': 'motocicleta',
        'z800': 'motocicleta',
        'z-800': 'motocicleta',
        'z900': 'motocicleta',
        'z-900': 'motocicleta',
        'z1000': 'motocicleta',
        'z-1000': 'motocicleta',
        'versys': 'motocicleta',
        'klf': 'atv',
        'kfx': 'atv',
        'kvf': 'atv',
        'bayou': 'atv',
        'brute-force': 'atv',
    },
    'yamaha': {
        'fz6': 'motocicleta',
        'mt03': 'motocicleta',
        'mt09': 'motocicleta',
        'R1': 'motocicleta',
        'R6': 'motocicleta',
        'tenere': 'motocicleta',
        'tdm': 'motocicleta',
        'yfz': 'motocicleta',
        'yz250': 'motocicleta',
        'yz-250': 'motocicleta',
        'yzf250': 'motocicleta',
        'yzf-250': 'motocicleta',
        'yz450': 'motocicleta',
        'xj6': 'motocicleta',
        'xt660': 'motocicleta',
        'xt-660': 'motocicleta',
        'wr250': 'motocicleta',
        'wr-250': 'motocicleta',
        'wr450': 'motocicleta',
        'wr-450': 'motocicleta',
        'big-bear': 'atv',
        'kodiak': 'atv',
        'grizzly': 'atv',
        'raptor': 'atv',
        'yfm': 'atv',
        'wolverine': 'atv'
    },
    'suzuki': {
        'bandit': 'motocicleta',
        'freewind': 'motocicleta',
        'gs500': 'motocicleta',
        'gsr': 'motocicleta',
        'inazuma': 'motocicleta',
        'rmz-250': 'motocicleta',
        'rmz250': 'motocicleta',
        'rmz450': 'motocicleta',
        'rmz-450': 'motocicleta',
        'drz': 'motocicleta',
        'sv-650': 'motocicleta',
        'sv650': 'motocicleta',
        'sv-1000': 'motocicleta',
        'sv1000': 'motocicleta',
        'v-strom': 'motocicleta',
        'vstrom': 'motocicleta',
        'eiger': 'atv',
        'ltz-400': 'atv',
        'ltz400': 'atv',
        'king-quad': 'atv',
    }
}
reduced_moto_atv_brand_model_dict = {
    'honda': {
        'cbr-600-f': 'motocicleta',
        'cbr-600-rr': 'motocicleta',
        'hornet': 'motocicleta',
        'nc700': 'motocicleta',
        'nc750': 'motocicleta',
        'varadero': 'motocicleta',
        'vfr-800': 'motocicleta',
    },
    'kawasaki': {
        'kle': 'motocicleta',
        'klr': 'motocicleta',
        'kxf450': 'motocicleta',
        'z750': 'motocicleta',
        'z800': 'motocicleta',
        'versys': 'motocicleta',
    },
    'yamaha': {
        'fz6': 'motocicleta',
        'tenere': 'motocicleta',
        'tdm': 'motocicleta',
        'xt660': 'motocicleta',
        'wr': 'motocicleta',
        'big-bear': 'atv',
        'kodiak': 'atv',
        'grizzly': 'atv',
        'raptor': 'atv'
    },
    'suzuki': {
        'bandit': 'motocicleta',
        'freewind': 'motocicleta',
        'gsr': 'motocicleta',
        'rmz': 'motocicleta',
        'drz': 'motocicleta',
        'sv650': 'motocicleta',
        'vstrom': 'motocicleta',
        'ltz': 'atv',
        'king-quad': 'atv',
    }
}


def return_model_from_extended_list():
    for brand, model in moto_atv_brand_model_dict.items():
        print(model.keys())
        # print(brand)


if __name__ == '__main__':
    return_model_from_extended_list()
