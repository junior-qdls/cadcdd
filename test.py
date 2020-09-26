# flake8: noqa
from core.optimization import GeneticAlgorithm
from core.optimization import apply_ga
import datetime as dt
import math


def __format_date(date):
    return dt.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")


if __name__ == "__main__":
    places = [
        [
            {
                "place_id": "ChIJ11Ju5iOa1ZER4qOyQTtGyVk",
                "formatted_address": "Av. Gran Colombia 242, Quito 170136, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.2146667,
                "lng": -78.5024237,
                "name": "Parque La Alameda",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Avenida Gran Colombia 242, Quito",
                "expected_time": 46,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAgtU-YGhyb-ksmMJKmjjVRYiGzW4kzgh8qxe9F9vP4WZm7KBntE-41-w6zV1YgL3jBvXG15M4hl4701iMqXWuQNTuHBNPFc_dLDma6bCLPUNaQ75RP0DkU29hniepWurREhC4_3uyQHHXtnZ4srb-KWigGhT5RVF5hfdVzBFd7Te1Jn33wC4v6Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAJh3IGZyNkHw1emVeLZFxtRrFqOafaVIv65twV7kebT7QtI4_D6YvM47kxMOXpiu7QL6lgYNrf4zft_HGO3-ByP2wznoxMBEbllt90VV64kAFjH5LB4wdhyw08vH6kbylEhAscE9Mzr-o-IoTE0ZfKo2vGhTO37zWolinNpcVnZtdvUcCIVqicw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAjqUmeVVo2ajTFPCkIQojsmtw6LE4txwvgTZhU9IH8gtWzydolRKrUP9NhTi_GBluTbSwFNM16LKKq9JIcSnhqD9yISeOOjEBALbHHQeXcLK0hzBxzyqMjvtlqqhFBvZVEhCM1a-aoUIIE1pzrDpFyXOfGhRxIm0kiPRcbjSRbsIdSRBva1_4pg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA3--pI0TIG0NDlX4d6MJrSH508HzqeuJU8clQVYPpAzq5mmCUKJonuSV-Q_3AwDDPjskd1BI3nHLzIaeVoa3Iyvnv57Kyl6rijiFtzCT6GZJ1_Yi4GExKom-z8TXU1N51EhC0lVoxEVQXikE_JNkCszZVGhTfQGENIe5gW3Ci0sa59c7Fvb9ymw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA6JdDh_o2R7O8Myw4P78wDrz-vyj5XGuAXSqR1u8bWKHkJOha81TgsrhLNRgO5UAuPrr-2Dw4XGDhpApKqfyCH4m04YiWmAVPfYkarS9TUB5LoIssWKBAE0CgHiqsZz1zEhAhXaBnhAfZqAe8TxYyrIOHGhQ6jRs8iOurleFdBvHL1Wz84oi5kQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAk7SPrUe8i8pu_N1RqJQAXxE4SuPiG3WJF8UEPX5B9NXWlUZFuMvlaV9BhnHDcQn7dibAIupaO0FNPz5_j29QF9QiXLvwLJsIC2Zdi5KIpEAI7ewk6qT4gyECjJhAD2a-EhDo5DrIgY_NxdeFHJHCIwzkGhRJCTke9qDc9pyNiEe0rZG9RVbRAw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAdyQFwkNy8GndvP0YyTAWt2KLYIRtc1bbvmnBBFLKvc7D5qsI7Hy6leqMhwSkFJhAyoul3cmO4V9ER1peh9hjoZeix6JwtUCjtGVaBZ0YI0Nuy4HXeq5ngzG_8AwjD97lEhDJ6pm5zX8UXa22iIHcB4fqGhTx_T5p2z6597FmRP3dcKYjD6GFVg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAABWwn5077nlStZVjAUECvvnN1Ghpxmtev85Jg6IGTn-nn--VA212tk5eOmRdCZFEDfrqxmf5kL9By91S8o2RDJBa5-PaRk-UnFvpn0Pm4uTDvxDhOM_qesTNBtp05WYkdEhBe1HOFcvoebBa87nk9Jy7rGhRwF2ASgY_pg4fLxfqM10SQ32tmKw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAt32aQYxjLxYELmOCvC9Q1h6OTMRqqMgl6Ko5033UY8JvhZDjp0cvIZzAgC-eF2QRo5_S1cgHwcJEkA3TXyjf4N940oJ2HM5Fp4h_qR2ocHy0E-_LATvWtAEyjXkmMjaUEhDrZabWfRCXSw_ZLse91pawGhRbD2yn_wnJty_-v4VRLzeNugtpHQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAEscMT_6jisjT7tNcu_CtVXFaZttG76ClqUVv58B77hlfABZtkMpQj2dQqOnn-Pwsv9fpXT4RgQ7SoDJXeRTpl8cwDriPB1otuzrWCU3Y7X_gpt6ef3ZNHVpHaDNmlL0ZEhB2KcMTV_d4tTCOS3n_igP5GhTTEblonGzuelSo5mfeol60WFFnrQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJm1GbfD2a1ZERHKCj5t2so6M",
                "formatted_address": "Quito 170136, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.2091555,
                "lng": -78.498611,
                "name": "Parque El Ejido",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Quito",
                "expected_time": 52,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAhdOTkBHU7KS0oEzj2j1P9u6e7XzQPuUNYuH5DQt48jxwM5LP3NwoqtCnb34MnaA0NB17y5aVh2gOMMwAxyBjylgxVtW1cOOD6ydWi1CC7Rh4xVqIbckkx4HN8UhMRF5DEhDSOt3hIWQUUxgVTb8DhZfsGhT2KGltZ_ZLfq9KpWZa369sodjWKQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAUhWoGMrxYhmcZMuTDeXjj-ST21MfHoy8tyu7kLqEXmJK8lkZtJT1DS-TUhJv5-EqMVOA7UW8xTMiozp4CHCsFlltvkT2Jdc7pEdbtUcEpFJ-9YM2CRG4skqFaLrnGC1aEhC8CTmtV7QV3NAy6XXhCdM9GhQ0vB4AjFK2gTLm-Uvt23Pg-QxVKw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAIYcIHfaU0zyI-gI8u2vX6B-8taBcpOwso-t2adjfe7lG8yceArNTUB0nogwB54A6LmEh291yEKWhWwqQhL80JuzMGDUg436y81ptt-I_siOc7ni5op7veh72JthixDSeEhD4-j3YJgzN9t3LnV3Ny_k5GhQtmqclVQvgTj6x0fqT7_VH0DaqCw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAlc-2-8HiEOpKRgRFC34-dUXvkFJlWqQPGnHy3VHUxDmhGGffHH2rMHBKlQY-63qpryzEtK4xIzyIv-IBqTBa7yl3TeIKG5H6ryDHGPR1iFDNnwHj-ijSk84Pr0-u0qeHEhDx8rYfgEbd_4Tw4qpgLWYoGhRY2Qm6QvOKeh37z70vdUyFkl-4VA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAZtRvIkb-vUdBFmj8cm_MG2fUY1GgA2iOkQ_0hr6vtV2x3aM2PbETMGQLEJ_Vo4duAE-DlAX30O-9tukuhb1H4XNltZZlKiGcgJlRwNrZ9fPioZ1FscYHO8jPl0ohzewgEhAF2nuj9kZQCDFK0USbmhL1GhQi4Z2MBF-XXNeVELn01Dm0KQlQfw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAjcucgSKdMcdYmmhuRgM8KGOdUJ0D_4MhXw3xhnGqCQCPjBk_UcOoEPVtZIs52TQYDB3VKfE3lZg_s9uXtOROUX1FAdONe-4eBzryxGZIsv-L1xiMB5-q6Tg4CzK9iZqDEhAYowQXGov1vMvSx8JW5UPqGhTQH-xvksd8qCIpfTOBAMe7orDUiQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAtu9_Xkk_yh3g8-gOKwmM0oeQyjjvtQXbiEEW9n4soIw_pmo-GXRHOA04oGS0-Zyt6FEYy-5A4BdVvFl_cW6oQOZy8KZ2wRwUmpblTcZDy2eLyeqpifbiCxSGiP9vp1cLEhAIi9Ei9ImjOjiNfz2L5MQ4GhT3XSYmQgSE3Bb5wRlO8uJ4JL9y3g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAT_lhckXpUboeaShJ2m9En25FDk4r658pn-zuxNuPlPyzFtWP1vMLu29-c9ugVhqj7GsXUA_fi3klFuGRk3r8IXdHl23RZDIVwcG5vC44--qzucSzHDZO1AVbgTiN56zsEhDEpSZ0xH594QJcQB4wkNKPGhQc6eLDWJNBDwfes5CIh5mpQkpp_g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA9MgZZmCP2M9TF4PtrH5jkZ3P8fMmOEEbI45fAtMWrQTolc9-VDYZXmUdzNb-FBAPssU3NU0dpgmrNmyJi9mfkFxMTfRmM5_v5lIyxRjYbtLZR4QxCx1G4VFOSLg0XwK_EhACc4FLzTHVHmfUduovEYXyGhSmiKsP4RmfxTdmR7ZuP9hajvtVWQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAk3NZrr5v_AkxsG2OF3XB4VhwDeslMdWi_IF2cgTnBufV0BX6zW7CUGSRJDi4MM25fG53um9L23jn8F_9Lrt8n17RxLhp_DMxFdU8zCx71hiaqtGqFqJL5Z9lBGO8wK0JEhB-ROaIAJHQO7bKalAjec5LGhTKQ53SJQZSLSiXR_0Gd_2umKyo5w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJA56fAjqa1ZERfPgFHGjxMtw",
                "formatted_address": "Miraflores Bajo, Quito 170103, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.2061903,
                "lng": -78.5086709,
                "name": "Parque Neon",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Miraflores Bajo, Quito",
                "expected_time": 35,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAO3r3bD4VrHYDFpyZ0rMZrSMNA-P5Rutc17PU5qRLfcJTa1gXa7_fyjfq6GPfgaKJxjZSsSpfBZ1LDL_DVHvJ_UaJ5-c4_esCxa0pGtSbDg1cDAvc6BRXETEdne5qFL3sEhACoDtKcyj9ggN-1XycpfGwGhRGhvkAhAnKaF_b902e-Yp--n9AvA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAlNKB5xShprTD88GR9qeAV_aG5I0GDYxoLydYk6q5u6ZSRuXUr9-svSmiiDG4J8nQZW_t8UoJh5Jk3qLoI-VmiUOZFwLc2lS2_ycr20zgHQbBXHQamk43lPv8VKOK4esaEhCjWV89qKAOONmSUnXbioi4GhQ3VW6YsG-8TNmXtwMnkUStxlWOGA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAATQll_cKQTJi9K6PLAr2h0dE1CSh_dUcuXqnFMfKvHjwa5bDJcnC2JM9wseyqdnqM6C67rUAPwraejGiTDo5jtVuuYZjG6qEZy5RoqTJMf7OSohw4PohJjEFH4SPKF9n0EhBWkqunLjLxDhhnJDmlsJX5GhThuu7SzPov5HhMpF7koHI9EeUxZA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAKLgSnMNdlRF6Lnu_v52lyIzrjQm3nLOx9y-_G-Hz-Anbc-FfYAIgKV7oP1p0QOInO0QFUqnYUCNCiiMlEsGIvFPmX5IzLym3aEAlubADbcOScuSYCu972W2TozZvUxAiEhDKjgCuF3dPvxthlYFnNqLoGhTNpSluPH9kLL5NtjJQWxR0L9cW5Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAARKg1260t6TwqvF8Rw_BvZ-Nh-djniBgeoWuY4T_qXqBhppTnO83mU0AGWeafZE4YxfNb2J-RAeosawN8HJpqKv25O8B947TwA3MnskRziwBdf3duom7ZvcTJlaMtWPrwEhComDVYRVGpHBOo5b48Ev8jGhRL4njhHUQ4muKqIZNF_-j3T1JcCw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJJTe0obub1ZERwN308Rte_FQ",
                "formatted_address": "Núñez de Bonilla 478, Quito 170129, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.194397,
                "lng": -78.5055094,
                "name": "Parque",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Núñez de Bonilla 478, Quito",
                "expected_time": 76,
                "photos": [],
            },
            {
                "place_id": "ChIJEzM8LSWa1ZEREePMDpFNQvQ",
                "formatted_address": "La Habana, Quito 170103, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.2108737,
                "lng": -78.5070341,
                "name": "Parque Parkour - Jardín San Juan",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "La Habana, Quito",
                "expected_time": 86,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAgIGq0f669eUNRIRLVzNS4CAEpRX1o9BZO563IdY52aX2_BrXWQcpyIwHahETSnqy87G2j7qPo_QgOrK00-7yjqzQ76MdK_M86xfXj8uyADd6EyFnAZthDEjrq6yZ6UnkEhBv7LPMcYcmamV-4JdgMZFAGhTszUJOTK3g0Uu4bFUAeiLzfjzhYQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA7ON9IqatSmaxS23FRFNqmU7Gg-1-vYIGXBTyQ5AnA2QFXRaXC5Ph0Qz0Q7jsOLDzzKBlkpMRplocRKfALAQPsp8QbjVauNFSpR0UFToHdqCVeSmWHStn0nzmVeTA4w_2EhDXSW24EnuGd5kBlexW3ULNGhQnmB-dwvm-aBjLUwdvpzCnprQg6w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAll5FyPrb4CAeeeGGK-YH6eBud_Me_MMNrEL3EXgjsqGkei_4jvKqjLWq5mwCS_xQzA0V2sQUo6w3r8VvXDYz2alrsyx0da-YWegm6bkGnZnImdGXxU2Ih6G2MQGgF_pEEhDSd3EJoSAxw1MZ09GFy6JjGhS2fA70TcTxEOYU88nigmg5DWpEZQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAdTdXrtkgp7kbie8E5GHoC-AeU38IFiDFMJRCR9l7Y3segLRr0Nl3mOa4l-xCp97-8HIp2sWa6crLlohI9KWvcZke-c-1q-jX-ZHcfERf788OO1L0HGcQ2Gz1BPiJal05EhD_viIRYjD7uteUloSnsGIBGhSz8wl0NIQbfovJqxLrjGNiSoUM3w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAOS8NgGzTru5N6PiPGcVpC8ZSWhgzuNMItmqiJRP6WT7yvB9ilEVaYz2kLPHF37ANLyoLE1XvUmZJUWDzjbxTUrcBVE9pCMKpCmsodSmsq4qXm53IXr-6Oe7Cmg_Hg6fJEhDuG3TPzBG8kFYjn5gO1uImGhROqweWDcKfvuC1u5R3_wbquGFYFg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAC5sqoV_TYBZ7FG4ZN1N2_2EcYVv_RdTeMWI2r9vaT16XNbae9KBfldkc6ScNC6z-F4cN4Gna0XCWGANZmV6mCdhbxrfYECvBrVLGGvdBBi4fSbIDGSDvjvfy8j-IHIQzEhDNeGp7mVIwCHXsDlQqXRHlGhRD0dGa7KdaopAqF8l4xytW8L673A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAEfRIPGQtl8lOq_KgZhFqvNvRVvnXMriBbt_v8yWSV6t-zROQt2Vjd3MtjPFoGu80IzTS89JigzuGTy-mpE7JCkNZ_qSRmvNgQtlTDf0yfxDtODKvh33E5X-DWY7rE_wnEhCACa1uY26j5mF4-uPMC6BBGhQsUF2Phu3w5_xkovbhfcuXAc-ywg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAnAkGvbdOTkIEcrOFHNjZtPalZUIKCBIy_dc7Y4V3Z4vdNgx_1T9GsznLkGngfx67QsWv9C5muSZomje8d-oYGFyrstVxiZBgdY1fw5oKnOqT_zsbvqbfUPs157qT1CaxEhBMnFJ6uHsbqjsXWRtlBWyaGhRAb8_VSnsrk7y3Ia9jaMolrU9wBA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA3KIY7EYlSO36W51-auF510-LL1bzE3S27faH5EMo3WX1sb5LzGep2ki6GBpLu9b3GhfztBCyhPmgtGKW-XECRNyKyLESmZZQq0LqHPv0lQgFquqIQCyhO9oh1w55uFw5EhD1DWWYqqwf9kvMCs86UuovGhTfTH7qlj-X8GFWS0y91M0FSZuXMw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAnUBlLXS77MdbnoUq2onVedax7R4_nIns11ZBSxnQKa7Te1EPELjK2VXV7exyD99ZXillUGT5D-CgjK3dl8V3zh3E03spEsiIfhevVZ-gw9pCMX6PyM9RgwasffWh0HGeEhBBaZ30Ou1pCn66pYHF9D6yGhTSgugHTC8vxghBCsxG_Yfk0iYg0w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJg7TbvDua1ZERioaLORWaZRI",
                "formatted_address": "Bogotá, Quito 170103, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.2078563,
                "lng": -78.5052336,
                "name": "Parque Benito Juárez",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Bogotá, Quito",
                "expected_time": 55,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAATe2WFZfChy6zSgaHRQRKyi2Mc4vlNwZjyQErjyXR8KoAYuDoKiJ-94MOG5PDrq0Yw8a0YBcWb3amUEJZI-NVHRaavimfBsYutUX3L-Jb7c3Z9MCbYnJfGd46_MEn0ilOEhDV9kUhWMuj95kvNOFe_aczGhSTg4hJkZAkCL9e9bzDf4lFDUkfAA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAQws0zItPmU-znqUZha8F008Lof6QvrkpPVYyey2m00Cq1zNTD4b-BvKSkv-QFENmcXeFshlhAguIoITNVfwkIexDiGioinZ3dqTRR_4bcQ1BnGelz35ezaIeBVJz3V1VEhASHbuPuG3VRVxQYsA1qbudGhT2w_vOyoXdyQKg48qmAd0uftoEJw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA8JZhJ4SE8TmorR1n3BNBCFSBEne-XhKuC6OD-_JgCzF5dh4Z8OaLSfzr03AxxPdtKbuiJyU4_iKX_WkcTGzAL4UjHwdSS0py82vXAK9jSHL5xilof-EDhS4GVMxAfEZ_EhC6pgtlGvBOwV_5aMwkbJdSGhTMfg1AuA7MWcYSuGenjAUCto-8ew&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA-H7C_HghE0D6Bk2RhC1_Sbfvmg039rksx-rH5RmMBAjfM5RTuqDQFSsevuiuzM6nyliXAtV4GCU8XHjIsUCxpdMmSAu6LBLxYDJSbf6IIcNMsg0MXQVUOHtGrrtE1An8EhATKdqlcyptVc0XXkStfmPaGhR-P3jYYnvm4GcEUoJFtrLLXzbgpQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAr2Jwz6yv3cDKjyz8UbYo9-stTNHTpq62qQkEPXcGMkA6X05cQD9TKP2CDSxkW7AjpDU_TRPCWvpO4M_1EqX1v2d6O24vvZ8x4_LWOXU3Xd0zvf0ptxq6M0JhVSbaKy6CEhCyE1VmCbF5PL1aBjXAvgPUGhRJQHhjUL94CEF4DQXmNiwAU2nrMw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA3sibmO9IMSiOSEFDxmWPYa3KV4utl-TlBL_0ahYDn50JlUAqnZHnKSOiE08FZUjjat02HbyN3_BIGdrF18_pRil-kl5m8E8SkSG1BSIB8yNH0BSRxAhrzQ5nhmgx7H_9EhB17ThE1WfjiGzpsmM0NY0cGhT51gXiYbs8xVxu_7cwSJuU_VC2sg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAx7MGIcltYTo2bMz4IKxCzkbvITPlCMQ3qHrXieSPev9I28ROUpFnrpBs3vlL5ev9SeTb-i-Xn9Locw9u1LTxEwKqtlAKUfQbD6f7C298bO9gfSkG1CG0w3qnFOKf0Ds-EhDJicE7ldHLTQnPGk6Zj5pYGhTA8qM6Uo5TLIr8a6UE-a7idCp56g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAzXPedZEYA2kZaML-HPW75e873aFM6AsKXhQ0aHdh20xTskuZetLCE8vleTStidmJL1c_kmBXnUBsVH3o-GQIX9OsI-p-gluLkvpJiE2toQU9-VMgRYiR8aIBjFLyIo2nEhAfZ8Oc2QH7nEKxZyeJh4C7GhSsYjX7Gg-SRs8p7OvVUqBzWgI4xQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA_-2kuwy3kDCIVOYp5HHuC743KA9C_coDsDQKChO1EUTXVs0cm6aSdMRFylLDx_tGvfEIuCczFanesfnE6-brOL3G3-mXyfhLb-4SuRd3x-WtIEOli1vukDOdKvk6H-Z3EhCy3aoTYQc6gwyd1M5BWsHfGhQ6UfATvAGRidUfN0KCBN15MMZ6aw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAALeqnimxTmuG4rIWDGl-ptGAGcv1ZQHrBq-Fg5SN0ry1DHfaGkKrK0eSoJg2HD6fC9vVDxSXXOafJZhzfQb0WHbmDpVvavAY3Vb1RZ5ANYHymOGhrELXgSkOoI-UycE7nEhBPqI_hvbfhw5l0pvnd1R7dGhTLgf-YvEcwjLXUVf5VTl9R0eN8cA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
        ],
        [
            {
                "place_id": "ChIJfVNWrIea1ZERE632s71GslY",
                "formatted_address": "Av. de los Shyris, Quito 170135, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.1813713,
                "lng": -78.4842769,
                "name": "Parque La Carolina.",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Avenida de los Shyris, Quito",
                "expected_time": 72,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAl_hQc2C2TPkVkC-nUokWt063-Hbv0vuBkhb1zuseUmqZoGzwn_bGYTZK9LgAZiKDxaw2BjYVW_-sJNsbgOuTD2tbAui2SOZFScPytqr8aCxfiLduaxmyb7dyMigyb1ADEhA77dnuWDaxOLmCBNcoSR8eGhT48VLkeGc62bklPz3uP0hQvqL2_A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA5_kNLYI-6fR3gmNQkPHapc2ChsvRZWP9B7fyGq0cjVp_7fngwdTCB5yF7kSAwcV3tzsAqia6C2L7_a3OqGdX-1tYgPw1NMqRiahFe5GOpcnY7Zn6cPA_vj7D5ybqXXSaEhA70txpc1ygs9vUimN1DW2EGhT9s6yA-vFnCb480QyGmo9vm-6qVg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA8tS6mQ4ITJKVcCnvJMj7lsTPNz2CVeXpXFMwu7C8CfOxcmvdS0cEjthgt2NZnhn3633blVX8kKPz1K29zo490hLk5vQxKKmasOUgScXBWSVnVcIIaMoTV8hnMdleYOBiEhATPIA2BO-7b2dyS7hJ9Cg_GhQfuek5OzPEq7zDRMM8Qm_3I2GgZA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAArDOP0L-QwXqhdW-biI_DNwEfabHPcsC3R-8NnqQQi6BaxquPaB97YY4Bw5-DSykd94JQWYe_VKli7Dl4a1oMTE9-jpwrWgtYGh4dBLpl7lmxWu1kooYywTCTSyHTPv7QEhBlWcdpeuLOiY0bTf6tKi2XGhQDx1PcemeBHiH2PtqWM7ppCiq6Ug&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAuLZM_EVXf-f1TCOhuZK3NjIlafV9NmOBFrtchPVKOggFQbGiS01dm97tQADrFWZH6jAIuFROOTMJ2BpabS6-LfE2DpZq2DSLSvrVQhlfHgS1ctWiCO8ThVKlE1NmJlGtEhALxKhFUJwmzWb6d1ZiuINCGhRL8hxM_sW0nvlmNMwogzcLPMOXlQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAANeJZRKL7AsX1Yc5EYa_NxZAL62sOW3ikrs2avF9_41BD7wHY7toOhgXp07yoMDt61hUVfDPmlazs-hN_N2SvEuY2vXpQ03DwnFH3igN_uNtpkJ2eW0oekGxQB4LdJ2hKEhAqpLHY5Wi-bwKz7MVmP7FOGhRt0vdtIYRSy1nEtdf7XG6jYIR5Xw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAINArHJGnp4Kr5IhK3NlMJjnnd02ZAFUk4y0CZj4sN6agHKEBNCz9v1S19bqaNdBtSSut93HGy7_1O9XYVnbljqV1cu6Owp-mgheAtda1IHXzYtHxU0hI8RZ1OQ6TjccaEhBrjllKBdfw7qIbtNRQoswRGhRLz9A48fclKIdhDSeDP2_1S7dsIg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA6nbiSBqp52O23fi3xE1i7vd7Z9wCxTa4AhKD2WnshEhh78PrZ6BungkNBLPGAByvH2Dc9WmK9zYoZ_HAlQDH3OUcK_cdC_JXZuzHqa9PSZITNWyjHBFpkB9cTl0g40gWEhC0mp_sTXo0EwJzZhOzVIKEGhQqGSzP4bpbzUaei632Tlm1xUPEsw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA3Vu4RIFrfMJ9nYXKkhTyi1DVVQ2FdxlgMpUbdBqazD4nTGGOduOJV76nWMWmqM-u3Sg0na6PfGJYuKjd5363UR6JXMVV8RjVeBssU2i0J9xQd-QAJx43OP06Xl0FRGD0EhC0X3VNeAtwXC3pbNc1XcTjGhSnNl5sB2V6Ldi46Ou_5Ww1WT1G5w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA-6EvXRcbm-eqql7oyOLrTYdewLdgOiC0KuhhfxWOuxiyV50bZaxJRzHU5xMoWoawF2eTPQ45VRNyNbl9n77DaoSKx8qw99bIepLE-KMk4iMkVX5rPyXabE9LGIpSZneNEhCmGDNljYAj71mKJGQYmRtqGhSAaKHt7H71eDZCDXSNDPFWcQv1Rw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJGUq4e56Q1ZERdH0rLAWfd80",
                "formatted_address": "Av. de los Conquistadores, Quito, Ecuador",
                "formatted_phone_number": "(02) 323-8834",
                "lat": -0.1968675,
                "lng": -78.4726878,
                "name": "Parque Guápulo",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Avenida de los Conquistadores, Quito",
                "expected_time": 69,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA-V0UazxwvzwsgbNvpV3RTeOZV662eHbWkO30xyAg0lcvdF5ZPozvwcyw0EMjgIvPd9yTHICcvien-GaOej5ELqD4JgWUrrvgBnmpD0nwfdl3XlUMz5DvlRZ5xdMb2gsrEhBOiV_-mLJOF7tWJ3ZrKQCuGhSmQydN4VPOZiWIDyRbns1_3eZEJw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAv5mGjHiiPbr0sRXIJTWQf8B1GXzMcltDw7rZLZTzplMwHkmbj-Y8pd6dhX6ZpbA7uJ9fCp_qe1OGNcgIbQ1eaMnAwxuURN0zVVUXDATaoH914s9gjZKr-Tc2ojXc3j9qEhA3SnqC_YLjCnwA0G5bfgtxGhQMLE0vOlQbeV4wpYHyfrJqLQcbvQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAACTv6OOftylSGo7F6UzvvjIW-vGLVWnK-9KCWQa9bXEU0ar6ntCyZVrvcFFZQk3uh17HmBZwrqZivwoeirdTGji9B0rhfbs_sbjNuZDqtxFWV7WnE3iBiPEskg5ZAScOBEhCYUjzxdfXfweE9RZeF2jwOGhQlwUbCpeREL-MMh6j6GRhYyphsbw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAyuly9S2ARoZ7qaJVdQraDqeMlwMCjtQ41zNO6sOWQEDyaE-LUk21lEGxkS3tX-mZfY-4RgDX4b8-i1egcg_mPOdYjxng1WXjWVENRjZW3JCLlUqQUmX-ulDcyzK8q5ApEhB27QsaWldWeb0hKF9S3d05GhTXH5sKhZBmk2eM3n0WkFQs-RNeIw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAHlEyrFm4UuZ7ueex3MsGM0AqhAVkFSGM8bxllMuH3fnJfCmoSKSjhMt19_bu1tHNQxeDQ56zj2UqtFbPs8T8lv370K6PZh1oiSHxJHOEd-e5taOKSG7GNkiVeZfrn_l9EhDV8CYqmCuzhqmSGu8SmHbHGhQH-CycgIuQn2ecXr5qrb77oCMxpg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAsGJeW9t_lYGnnqbeVsfctD2oEXm_iFeRHVKqh9mjcyjgrfWiFWeFaY0eBCu3pBmAIgGuBBpPA8z1rAeQ4AsCyTNE0WKr2bxeoi9vOgOwmlOuxinWJoSr1ovJzfx4zqR2EhCw6dOv5OWGgFoiwLDepIZbGhQgGv1zlEM8641R419om8ZMLM36zw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAASZ7FJDVPkuA7S84Orqhs4n87lOVSBsQ_CydCNa6Svr0ZY5nkMXRJF5WZJzLGz8T79DrEIiktYTWtMJlRjH_1jVz_4-MUYnnwivrXaVvdKMF1bRLTUA3UNio7NwhSlFv9EhCFHlOBjuJWaQaIyN22KjQLGhTv6YwB4Qx4C8Xv5Oi4P0JLWNIiTA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAqNg_43tzgVCxVcGGF1bWa5rOGMamSj3NPRPax5EETdNsqgs79DfZ20mf899_97Z1VVTz-iHYSUZTUpO9_xhUXwD2yTLPGxvyznXo1V9_N44QPDKEGsH1NpjJ51fIz6AlEhAiunLV5URQWvQw2gD0FEM6GhSTwn4N-3poWjg22emV5hUwmxd5ag&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAopaBzzS15uwKi7226ZZKsHfqs8HllgCbOE1YCgXGZtHGzabdfydBWf5UTYLoVbZ1uf6Ji3jXJY7DX8yhecNfx7hWGWZDRPMpMgjTYH22-iDZ0zw5Se_Xr62DTUcZdu4WEhDW89jQAiMvgZDT2EXk_MwTGhQm29ySRbxvbTl-SXFrvGqjRi4mUQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA2rCyaDyDRP3sbwaM_CVTM4t6j4qOIIpne3Lqhubuq7Cjr9e7w9i2w45IMv33ptmz6p6eEbyzZctbPpNvXcTsDAXBVp48n_c9OilwPHBkfTXl4NidgDd3lj08aw3-YbKbEhAYpPLWY1R9UxBrzftVwi-bGhR4MCiNUSrA9j6GYKrEZyqPg9cR1A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJt6Dp7X-Q1ZERlnBLXm0ivdQ",
                "formatted_address": "Quito 170135, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.1823707,
                "lng": -78.4740633,
                "name": "Parque México",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Quito",
                "expected_time": 46,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAYhgLvvW4PoYq_6p435wv6W40KCOewiOtb1BM-uO04AoP1aBMwCsJ7riauohaT0qyiCI10KKwTZuBHqhQFQC2aXJVA_tJW_YlvpiijqtL2G3vGbsoGcBemeHhXeWN7PDlEhDsbMRnZOdQlkHD_qUx-zB1GhQX_R-WlO9xnFvPIZBO6olFlyaWBw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAmPnXzsIyQDr8BDMUmSy1kGYsmRC2kqxir96TsNmQ0wHNnyfrTLBTDt_bBPs-aRDmUnJFh4OuDGGDj-wqRorGvp-KrSRexm3Hal4jq0bVVAIGyeDO2Mz2AbOknZyQtpEkEhCmC9V0xcL1byc-GNNTbXxIGhTX0tTiqLWd3IKsS7OmzLqSbA4jAQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAASaN0ZzrZNd0b_is4dkb9OIpiZlKJrR88QJkA9IrviKzGnNzIxwp1ZzAnOs85vaZAI3DBOpdAsvq3eYm-YoknyCLAAbshk3tzrsjdRwyd2a51-ecjmvFZBbYWAjP88T77EhB52PNBjHKoLfzBmU8y6BhrGhSQuWNFzvKXyE_aqFoQYhkP0-9rgw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAFIBLKEdF7jRhpAGkqXLRgy26Up_qfXF1lSU0aw9QG7H2lV164aWdNPWvb_QjqWlZA1RqtJtGkg9-HU0fW9eKyFI3tSmtTFmja0PpMONYabqBQ9hV9_kGei_dNtiQHPU6EhC5q3wYVndRxZkPOyOaPYwmGhQoNiBX2MvWEh2lzVYn5zFM5igTfA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAr1XEwTXCQ7yxT-jfj2kroR4646MyFUOb3M9ULdS4avvrTlRT9MV6Tz8PiItoASl8kJLeISLLEGGDtagG5nclH5GimRSVHpkc7ivqZzcpbQC5aig_rVOLBvTqiygKqquNEhBeUoqwjV7M14-sudLbJF3PGhRSVmJZL_Cjn12bmI9tkuti44hvNw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAfeZqZo9d6E03LmOWZSEOh0MYx5on8ShQFKYQg25JZZVTCi6NfNPMYD-WfxiQ7csgZLsNJ8KaqUIviCe3swlXInvTgvIZMX9hJyMx73nXcqttzxdOtbKr9O39Y_C7OXi2EhD-fHZ9bUToJ1iommBGBJFTGhShQ0iLAAIFcLCzRLyh0jrX5DsmBw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAGlTJB2MDKVQ7oW6tgEdQ-wV5GAeR6IjdhLpOqLY_mRqKvGH1raLVH9Zz0gPaVnMnx44kauwXegjQO1Nfw1S96P7LzDy3iDOzNbXHhQ3Yle7rIOAFdfrPdg8cRG3pU7eMEhAI8Zt3B9vXpXHJ3h21v_aQGhTIKyMP-UWV383G11ytmi0S1mPxmA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAADfV_EziYr0bRkDiNj9Cl9s0lRRMSiMHzyVPvYp3s2_y4eyWb90kafwO5U3bV5VXJ4nBLN5il0HytViqxF4UpzLN3svagkTg_GWva7NCyNdvSZxjplcCIhh5SeE215aQcEhAWvGJuYsj17u8N0dKqlRzdGhQCJPMWto5b09sJct6wTQ3HbNMuqQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAwZidAWiN7q_Mgvexcham_d8daytANhHlNub8Sn7J07NPZfDJ5LS2KdHXLK0O76iFSQnjQw5C401Q8VCk4T32Z5hyYdE94ue_IwdL8YnftKwoScPkAlv_WdpOb8h4PhLTEhCalpc6chwDQWJoGpqrDP3ZGhTNiUXN6pM4PtFOXXoSfodJwr2hLw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA4xqhdB_xm396bTsjCfGQSodAFrLzmEBNidbLjiUF9GeMh1qoOCR8VgldxpMlcBspYwG44oQzC0L4uTaSCVw3xI5I19-Gx65B3p2RRTwcG4baf06sUmhuP9b1oCHfQl4JEhC1B6xRUeSlvgPy7wXo4ej2GhQhDRMXFu66DL4RkQVQLHn-kKXpFQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJZZ6XCYOQ1ZERW3k8QSUDP0w",
                "formatted_address": "Bellavista Alta, Quito 170135, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.1901699,
                "lng": -78.47111360000001,
                "name": "Parque Bellavista",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Bellavista Alta, Quito",
                "expected_time": 34,
                "photos": [],
            },
            {
                "place_id": "ChIJKR4Ww3-Q1ZERUkpea2pkR8c",
                "formatted_address": "Guanguiltagua, Quito 170135, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.1823272,
                "lng": -78.473255,
                "name": "Parque Guangüiltagua",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Guanguiltagua, Quito",
                "expected_time": 70,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAB_YJJaY8XCpwjiHWPIZo92QU4gYYgXHrObmj6mlppEQmjjzDx1pDAN8WZfJi3wcTT0dndVMhs61z0IAbmGLVlHO1hfPsjBfXUe0uOYjl9Yh2FbKSl2dCtRK-C0evY58qEhCHyKuakT6U2_a5bCZDDepvGhRxPC6LcISHpqJ7C1ROGiX4NQ6v5g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAADmlN3189R4JYInzxNETpqPfCRF60QnDt5ZCGkJyJndbQ7arF1h3fk9UzlRzAFo716aSQoQgwV2zdB8CGtsLy2mQQ8EZoL24VBBwH74dFAnyzcL9IxVHJxhohf6vM2RqQEhB01pULx08uys2qkUpLdUPOGhRDjtMj-UupAxcZNen8DXH48UH_UA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAvHtMft1xU7uvnm9yGWc5hupUn17fgOaEx4wpp09VLi_rmO21SlS2h1aNDabGdX-LXEzPS8V4huMGZRC-LIfzYq2QtVTYxGRNCWSdFWu7qvND5kHwJ9e-whsI5TaX3lPwEhBZ_v5IR9uHd7CGtchY6H7OGhQJX366HXPZ3o9nFMuAWiOtIx6TPA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAKcB0NUTR-_BUjfxc6-cQBTaGBQM5YgWMhcR2NbDZDF8b7_zqi5aY50RviJawLonX11ZB74e2wWXw-ZIpWInn-xJ8K0moP9TkmUQURszFAwwdybxwIiMmLfRM-fzX79IPEhDnI9g8svklRXcH9q2xPvyoGhQlHM1rr017VSCNSOAZjjewYsVdgQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAASibE0OPlCPNoR9u_zHdKpbK7CUL7d5SdTDa7lpdqi5C53CD_Bn85dOR_l_n6C1OyUPiCniz9Do-bJRZSTCqsopMh6FmAF1dUMpwar22VZwkz567g5qUizEzktL99GnZxEhBWsPb0oiZVAC88zYhBpdA6GhSqcuiqt4SUB33WmHvI-cQLRWAtHA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAl6Xg2IT-vKRf8szc-Zg4aEuN8z_tP27lgkpang7tNuKxEQlkNJcahfxx03W-lDtYHOjz9YVQtFxuw3je1Vn-v8m-w2PfIUO20nfqJulN3mEjINtgV_vTU4fvow62Rha9EhAB3Hg_geXV1BQBrGsKXWShGhR3tXqYEo-Ha26d7Tfpkdf2w5IT7A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAcbukBYakSxrcIBIMOb61pvM-vQSw_XQRWYgT9Kmjh33_OxmV8rLESN-Fhp60zlB6wx3nAf4t6cC9MMww7lBsd7oL4HVPLNlzvkQmAjTpLkT7aLbebn8c03S_nB_W19XQEhDrn39JWpGWJXE0kCI2udFlGhSDpb43_WsSCaKx8h4Jri_DaxFBzw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAACbORMWJ8_-IUscN3NUzwUnc9I6hm_oNaIJyziT4D3akr5qp8RKaipMJfwdHX4RQgj8h2dasu3NToI62Q8aNdc7d2W_gnMUUTvHlpZ1yVcqXmaBDUHe9Z5Je_wQLcaIN9EhDgA43f1_eWehm56H-ehK7QGhR4Wy3SVSEX1gsMdTvTtWHNTf8NPQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAASGInTQ3HHW4wffgL7GtL7-UwdhtmmtNn9DLv06tgm_W67p6RHdAPonrbGSqv95yaPKXxMonv7SaavFxNNuHITj8PzccrJ0Qe1YhYjfTcZgqeZEo0Fv2VQcxZHtWxNoceEhAvKrwMBcsNTWZsxzyzIRjfGhT0vQESHy-YH-LwsaYqPFcVt-O2Ag&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAa4r4-c8ExDexHZugEUry5CAOBmIfknag9QRmcm3bqlUVe7R_GH-CbmQh0iKPeRzibZq2ynmAa23EnVm74s1ofbEa7oWuSTgH14Efg-gu1xHJAwnRmGNLgXYdCRl53gAeEhB1pkekXbebppkGh-9frV7UGhSbUAqTp__Smm1G_gEZakViX1Q4pg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJ5bYu9ZKb1ZERwv9UGiCea1Q",
                "formatted_address": "La Merced, Quito 170109, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.2054135,
                "lng": -78.4797336,
                "name": "Parque Feliz",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "La Merced, Quito",
                "expected_time": 83,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAACW-li7h7gRJGXh8naVCYj1k16hKM_YsGDQZoPLM9Rt97zxbiLmwXIBQV-_30Pay1wD1ficgEVd5qIV1WhmKIE5b0KfMkOMiYRx31-Q24tftCtoDDxnlmC22lMxCEzPpeEhDh1SLVb3RGAPtkNcNur8_eGhQzFv9YoFZgrrmz5KfuHbv9XjCWiw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAASF-6UhgdXnyQMhBqj3hKhEnwmcClp_J-Qg10az5H5KZdvkHOEBEiwDIJZ1CXRK4aom9Eec5pjbghJ8atV7P_as2TWXgX5T4UGqfHIhEj2wzNjmwqiwoBbVwDhkl1CSVxEhBlxCUjPEAy-su_CckzmGR0GhQc6ZPemWK10PNqtisFAeodCPB8Wg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAp-IFgZp5eP9dmuKqvmdevnALPNYh9jWKGhYsnBi_1o0V9cTnTHVlEUtCBqCTIsQ-FuFNcjOKMSpmDgfSyRHskW9jLG7ONOoTdb1hob_OMjhj5CMJ-0r7AeooUIAncSo-EhBaC59F4sMOTYKmDo0FetJRGhTMCKc_MSpHb8bnVqV6iL7wPpS2Gw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAe9xV2WT0X0YJVxYdA0iKX18drbSsgtG-jLsHXcwgSxUQJqvRnLTvWB95GSXr5JZx9q-kUf-hGArXexHY3YVvlqEyU3qNNKTRg_Z6eTYAxPYVCR_zsBqCjlteKsUjWYFhEhANB3VrrSJ6ovY-MnG66JdjGhQOQ6rMET73bpMSdqdSihAvmzGulw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAqeeUqP5iRH-mzdfBCJXYfLIlP7kbtXPPTpoZNViGwHbM-TCqgtZoE-DkPf5Ols8o4bUH1AqYSzxJ_CFicG8sg7H9EcmdBrc4rtrbqJEZF_e9_XPBbwR8Eq1MDDDC4hXBEhDWgSor2Flbml-DpvFjlSt_GhTEna4ODTzFQ4QgdaFiVSHXxoTgZg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAVzIslB_W9fX8DUsv_pW8KbrEBRR9vN0z227V88t2vVnH6iTjNCObcOskbE2h2Jr9o6f02-nXtHj6IaLUZwaCt-YYZl6oRpbwrLtHVS2uxJMmSnVvrFOZTWTdFIOsrDL3EhCI1T9rS1H8ihlzXGQsJXm-GhS3xB8mTiziL8qDiFy7c9M5WOyxcQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAb_1Ul5BSXOGB-1ug05rG-XDMxuPAqY2ixCZqdoYu-4W9pNuZ1or3x_G_C3jnL-9u74MaMQ3m9PG_qBJS1cvB3DmRc5AS2glc3BCbNzIPuhZw9R0kmOmMLMB8Pj31lBq7EhAlIJ6MDS0imDYkUY5SSNNsGhQ4OoAiQOrXdAzAfLOrjNnwjhncZg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAzwrYFbeKgubMkbEtJXI7_qBK5HBT-DQmFmCA2Ss1dKmxqSt0HWrRAN-RZr-Ls_-T3LNyLpu1SEugRKMVxjdof4YXxB4ADBuG6fOoQgQ8pe-mj-YsXxwmoEHP-n5WW_q9EhAFLAW8Xvrb8_3edd5XbKl9GhRTDOZP-gwKJYzBQgKxxJlE8npkvA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAAGkMr7tfkeuCyHvwhymYteQdQkpP7WUaksTJk1Rmlwshz0ZWwC_B8kpsZkQGKr4Q-FbJp2MFQIvDxFeNe6HB_9PuENr4ioIT9xZXotAEYo3aYlDPLdH_VmXSlo7KThl7EhA7qc_9rqCH68Tp23W3aVzcGhStEwPDZcQXF-sdA9yN3G7Qb71GpQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA_EMcUvQqRpG992A-3kftKnnRAp5pAdat013XkgO52gTS624X93YjPgcAzKtjDW4pdVFnS2iceUPS9j3u_VwDlna7H37wIVYfnmjlywIWWszGTPqmEo46hBDo4Ti3fnbPEhBRfApNjUpvPCY68WnfgzAoGhS6cZ6Lu-oKkoYKGqVs8XKJffq18g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
        ],
    ]

    time_matrix = [
        [
            [
                None,
                {
                    "duration": 14.216666666666667,
                    "points": "bbi@|lc~MmAsDm@mB_@eAWaAaAgCc@cAmAwBYa@s@y@w@o@iAu@oAaAKMKJKIICc@B?@A@CBE@G?IMyAE_CIS\\A?E?A?IFAF@F[l@UR@B[H[DS?A^Gb@_@n@[^i@Dw@@Il@",
                },
                {
                    "duration": 27.05,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPWQe@_@_BgA}@vAo@`AYTi@Fu@@[DSNg@l@]n@g@lASp@c@EqB_@wFq@kBWiEi@aDq@cDs@[jAYxAm@fCmAvF{@lD]`Be@EOAiAHUBQC?QBY?CWACAAE?Y",
                },
                {
                    "duration": 42.88333333333333,
                    "points": "bbi@|lc~MmAsDm@mB_@eAWaAMa@O_@mB|AsBvAiDtCGFu@{@y@r@]RSDIAQGcB{@q@WcBe@kAUIPsGgBkDy@eBe@kAYs@IgAKkAWMb@KXEJOFs@Ve@VKLiBn@yCfAkEzAo@Zs@Py@CwBe@wA[qDy@yBe@iDs@_Cg@o@pAcCfFc@`AIVe@tCMr@QdA_ApGq@`EwBa@eCc@_@IEL",
                },
                {
                    "duration": 16.783333333333335,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPWQe@_@_BgA}@vAo@`AYTi@Fu@@[DSNg@l@]n@g@lASp@c@EsB_@KNC@WAWEU?OFMVETCTQAi@GEFQBw@Gc@AOBQIWGg@?[JBNG~@ARDVFJ",
                },
                {
                    "duration": 19.016666666666666,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPWQe@_@_BgA}@vAo@`AYTi@Fu@@[DSNg@l@]n@g@lASp@c@EqB_@wFq@kBWiEi@aDq@oDw@ILGDg@PMGYGUD?FEDE?GEKDCAME",
                },
            ],
            [
                {
                    "duration": 14.216666666666667,
                    "points": "bbi@|lc~MmAsDm@mB_@eAWaAaAgCc@cAmAwBYa@s@y@w@o@iAu@oAaAKMKJKIICc@B?@A@CBE@G?IMyAE_CIS\\A?E?A?IFAF@F[l@UR@B[H[DS?A^Gb@_@n@[^i@Dw@@Il@",
                },
                None,
                {
                    "duration": 20.616666666666667,
                    "points": "zxg@`wb~MQxA_@hEn@RFBGT^JGRo@tCMl@uAtFwDxPs@vCKxCiCe@CZcDGELKH\\~@x@nBVp@HZH~@?F",
                },
                {
                    "duration": 33.2,
                    "points": "zxg@`wb~MHm@QAa@K[SU_@Oc@Ea@Bk@iAYWQs@tAg@|@u@rAw@vAo@jA_@b@]Zc@P}@\\{EpBoE|AeGnBm@N[BY@u@C_EcAsE_AaEaAkCg@e@Ia@v@m@jAyB|EIVe@tCMr@i@dD}@jG[fB}AY_Dk@_@IEL",
                },
                {
                    "duration": 19.7,
                    "points": "zxg@`wb~MQxA_@hEn@RFBGT~DhAMZuAzFm@zBw@pD{A|GbDr@o@tCABbDr@|@X@HH^\\l@EPAHBHNk@HDVVTLBFFJ",
                },
                {
                    "duration": 11.616666666666667,
                    "points": "zxg@`wb~MQxA_@hEn@RFBGT^JGRo@tCMl@uAtF_DpN",
                },
            ],
            [
                {
                    "duration": 27.05,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPWQe@_@_BgA}@vAo@`AYTi@Fu@@[DSNg@l@]n@g@lASp@c@EqB_@wFq@kBWiEi@aDq@cDs@[jAYxAm@fCmAvF{@lD]`Be@EOAiAHUBQC?QBY?CWACAAE?Y",
                },
                {
                    "duration": 20.616666666666667,
                    "points": "zxg@`wb~MQxA_@hEn@RFBGT^JGRo@tCMl@uAtFwDxPs@vCKxCiCe@CZcDGELKH\\~@x@nBVp@HZH~@?F",
                },
                None,
                {
                    "duration": 28.25,
                    "points": "dgg@dvd~M@\\@BX@Cn@OCBH@HAl@CLMRMDQAOCPh@Vn@BLCHKNIFq@CuEUeAKeD@aALyB`@gEz@]Hk@XqB`@yAZ_AHc@AuBOoFWp@}DLm@?c@?cCGeAKoAMg@gBgCKa@AU@eDeImAwBa@eCc@_@IEL",
                },
                {
                    "duration": 11.85,
                    "points": "dgg@dvd~M@\\@BX@Cn@PBTC`@Gn@Al@FxBsJl@sCbDv@lB^t@RADb@Lf@Jx@L@EbB`@JB?c@KU",
                },
                {
                    "duration": 7.666666666666667,
                    "points": "dgg@dvd~M@\\@BX@Cn@PBTC`@GQ}FC_@~AVPqCJuCn@oCNq@Ja@",
                },
            ],
            [
                {
                    "duration": 42.88333333333333,
                    "points": "bbi@|lc~MmAsDm@mB_@eAWaAMa@O_@mB|AsBvAiDtCGFu@{@y@r@]RSDIAQGcB{@q@WcBe@kAUIPsGgBkDy@eBe@kAYs@IgAKkAWMb@KXEJOFs@Ve@VKLiBn@yCfAkEzAo@Zs@Py@CwBe@wA[qDy@yBe@iDs@_Cg@o@pAcCfFc@`AIVe@tCMr@QdA_ApGq@`EwBa@eCc@_@IEL",
                },
                {
                    "duration": 33.2,
                    "points": "zxg@`wb~MHm@QAa@K[SU_@Oc@Ea@Bk@iAYWQs@tAg@|@u@rAw@vAo@jA_@b@]Zc@P}@\\{EpBoE|AeGnBm@N[BY@u@C_EcAsE_AaEaAkCg@e@Ia@v@m@jAyB|EIVe@tCMr@i@dD}@jG[fB}AY_Dk@_@IEL",
                },
                {
                    "duration": 28.25,
                    "points": "dgg@dvd~M@\\@BX@Cn@OCBH@HAl@CLMRMDQAOCPh@Vn@BLCHKNIFq@CuEUeAKeD@aALyB`@gEz@]Hk@XqB`@yAZ_AHc@AuBOoFWp@}DLm@?c@?cCGeAKoAMg@gBgCKa@AU@eDeImAwBa@eCc@_@IEL",
                },
                None,
                {
                    "duration": 37.21666666666667,
                    "points": "l}d@dbd~MDM^HdCb@vB`@dIlAAdD@TJ`@fBfCLf@JnAFdA?bC?b@Ml@q@|DnFVtBNb@@~@IjE}@j@Y\\IfE{@xBa@`AMdDAdAJtETp@BHGJOBICMWo@Qi@NBP@LELSBM@O@OXYTChAIN@d@D\\aBz@mDlAwFbDv@lB^t@RADbAV`@F^F@EnBd@Ag@IQ",
                },
                {
                    "duration": 29.85,
                    "points": "l}d@dbd~MDM^HdCb@vB`@p@aE~@qG^yBd@uCHWb@aAbCgF`@w@d@HjCf@`E`AjDr@hDx@|@Tt@Bt@EtAa@|E}AVNDJTT`@LrD|@~FzAbDz@s@vCo@dHzAVjB`@CHUfA",
                },
            ],
            [
                {
                    "duration": 16.783333333333335,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPWQe@_@_BgA}@vAo@`AYTi@Fu@@[DSNg@l@]n@g@lASp@c@EsB_@KNC@WAWEU?OFMVETCTQAi@GEFQBw@Gc@AOBQIWGg@?[JBNG~@ARDVFJ",
                },
                {
                    "duration": 19.7,
                    "points": "zxg@`wb~MQxA_@hEn@RFBGT~DhAMZuAzFm@zBw@pD{A|GbDr@o@tCABbDr@|@X@HH^\\l@EPAHBHNk@HDVVTLBFFJ",
                },
                {
                    "duration": 11.85,
                    "points": "dgg@dvd~M@\\@BX@Cn@PBTC`@Gn@Al@FxBsJl@sCbDv@lB^t@RADb@Lf@Jx@L@EbB`@JB?c@KU",
                },
                {
                    "duration": 37.21666666666667,
                    "points": "l}d@dbd~MDM^HdCb@vB`@dIlAAdD@TJ`@fBfCLf@JnAFdA?bC?b@Ml@q@|DnFVtBNb@@~@IjE}@j@Y\\IfE{@xBa@`AMdDAdAJtETp@BHGJOBICMWo@Qi@NBP@LELSBM@O@OXYTChAIN@d@D\\aBz@mDlAwFbDv@lB^t@RADbAV`@F^F@EnBd@Ag@IQ",
                },
                None,
                {
                    "duration": 7.166666666666667,
                    "points": "`dh@nld~MGKCGUMOOGGIEOj@CI@IDS]k@I_@AI}@YoFkAkBa@IWSUSG?GCCAAAG?Ce@]OG",
                },
            ],
            [
                {
                    "duration": 19.016666666666666,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPWQe@_@_BgA}@vAo@`AYTi@Fu@@[DSNg@l@]n@g@lASp@c@EqB_@wFq@kBWiEi@aDq@oDw@ILGDg@PMGYGUD?FEDE?GEKDCAME",
                },
                {
                    "duration": 11.616666666666667,
                    "points": "zxg@`wb~MQxA_@hEn@RFBGT^JGRo@tCMl@uAtF_DpN",
                },
                {
                    "duration": 7.666666666666667,
                    "points": "dgg@dvd~M@\\@BX@Cn@PBTC`@GQ}FC_@~AVPqCJuCn@oCNq@Ja@",
                },
                {
                    "duration": 29.85,
                    "points": "l}d@dbd~MDM^HdCb@vB`@p@aE~@qG^yBd@uCHWb@aAbCgF`@w@d@HjCf@`E`AjDr@hDx@|@Tt@Bt@EtAa@|E}AVNDJTT`@LrD|@~FzAbDz@s@vCo@dHzAVjB`@CHUfA",
                },
                {
                    "duration": 7.166666666666667,
                    "points": "`dh@nld~MGKCGUMOOGGIEOj@CI@IDS]k@I_@AI}@YoFkAkBa@IWSUSG?GCCAAAG?Ce@]OG",
                },
                None,
            ],
        ],
        [
            [
                None,
                {
                    "duration": 61.833333333333336,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNN@HOTMnFh@xGr@bD\\r@BVEf@I\\MrAs@tEeCl@Uj@Q^GbAVt@QRON_@Rw@PUVIX?rEtAdDbAhAf@HBHQTeBFKJGLAn@HTDT?~B]NC`Ba@NB@?@ABG?Al@IX@`@Fl@LT@fB@BM`@eBRs@j@gCTcAxAZzGdB~AXDQJWTSx@g@lCwAJETCzFCt@BBM?CiAa@{Ai@kBUi@Mm@CWAGILEb@Gh@KJC@EKGs@Gw@IwBo@SGGK?[?IOIYAg@G]Om@IsA[OFMDUDMAgAa@WE][gBaB_@QSAO@c@@c@MgAk@q@UUCiAWWAGAGGMa@M]GK_@UOOAKQ[CMB_@JSCOCi@?eAFaACi@Im@@SJeA@KDCJSJURo@",
                },
                {
                    "duration": 23.416666666666668,
                    "points": "lkb@xs_~MJG{@uAY[@UHKTEtAL\\iD`@sD^oD\\cCd@YDUB[?_@m@cE}@}EDYAy@F_@^m@n@o@lA\\nEbA\\DL?|@Sn@e@MYOS}Es@{@QQQM]SmA",
                },
                {
                    "duration": 34.9,
                    "points": "lkb@xs_~MJG{@uAY[@UHKTEtAL\\iD`@sD^oDRcBT?j@?vBPxAHbCPjBRbAHxDd@v@JpDb@v@XJc@DYLoBByBJiANg@r@iARa@Nu@HoBLc@FGTMfBm@|@WVONKHKBK?WAYaAkGlBKLMDW@qCCaCHaDhBLAaA?E",
                },
                {
                    "duration": 23.233333333333334,
                    "points": "lkb@xs_~MJG{@uAY[@UHKTEtAL\\iD`@sD^oD\\cCd@YDUB[?_@m@cE}@}EDYAy@F_@^m@n@o@SK]Eu@EOG_Am@iC{AvBQr@KJM@G?OKM[KKCJc@R_AvAZrAT",
                },
                {
                    "duration": 43.733333333333334,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNN@HOTMnFh@xGr@bD\\r@BVEf@I\\MrAs@tEeCl@Uj@Q^GbAVt@QRON_@Rw@PUVIX?rEtAdDbAhAf@HBHQTeBFKJGLAn@HTDT?~B]NC`Ba@NB@?@ABG?Al@IX@`@Fl@LT@hCB^BdCf@nBb@lBTlCXRNpCcAxB_A~@a@AWBGJKNCJ?FDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C?ABCHAD?@@@?BER]SYGE",
                },
            ],
            [
                {
                    "duration": 61.833333333333336,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNN@HOTMnFh@xGr@bD\\r@BVEf@I\\MrAs@tEeCl@Uj@Q^GbAVt@QRON_@Rw@PUVIX?rEtAdDbAhAf@HBHQTeBFKJGLAn@HTDT?~B]NC`Ba@NB@?@ABG?Al@IX@`@Fl@LT@fB@BM`@eBRs@j@gCTcAxAZzGdB~AXDQJWTSx@g@lCwAJETCzFCt@BBM?CiAa@{Ai@kBUi@Mm@CWAGILEb@Gh@KJC@EKGs@Gw@IwBo@SGGK?[?IOIYAg@G]Om@IsA[OFMDUDMAgAa@WE][gBaB_@QSAO@c@@c@MgAk@q@UUCiAWWAGAGGMa@M]GK_@UOOAKQ[CMB_@JSCOCi@?eAFaACi@Im@@SJeA@KDCJSJURo@",
                },
                None,
                {
                    "duration": 76.0,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@WRELALNp@",
                },
                {
                    "duration": 68.98333333333333,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_B`AGj@CDALU?c@@{BCaCHaDhBLAaA?E",
                },
                {
                    "duration": 75.68333333333334,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@kAW",
                },
                {
                    "duration": 34.56666666666667,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DdDlAb@Jf@@hA?|@Ah@P^Nx@JdC\\p@Tv@^U^IXCLEHe@O_@M[EUBQJSYGE",
                },
            ],
            [
                {
                    "duration": 23.416666666666668,
                    "points": "lkb@xs_~MJG{@uAY[@UHKTEtAL\\iD`@sD^oD\\cCd@YDUB[?_@m@cE}@}EDYAy@F_@^m@n@o@lA\\nEbA\\DL?|@Sn@e@MYOS}Es@{@QQQM]SmA",
                },
                {
                    "duration": 76.0,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@WRELALNp@",
                },
                None,
                {
                    "duration": 19.183333333333334,
                    "points": "dtb@n}}}MOq@@M@GHKPM|B^`I~@`@@EKIMu@i@SYEO?QBOJSx@q@b@SpAe@JQdCnAdBf@bB^?VvBp@jAFhANdALPC`AGj@CLMDW@qCCaCHaDhBLAaA?E",
                },
                {
                    "duration": 1.2333333333333334,
                    "points": "dtb@n}}}M[uAW_@GC",
                },
                {
                    "duration": 48.56666666666667,
                    "points": "dtb@n}}}MVxALXRLjB\\fDb@JLHLFPMJ]VOFy@LO?_Ba@mB_@mA]UG_@^]`@Vj@pFnA`@Nr@^jFnDxDtCTTtA~BjApBp@hAJB`AVbErAjC~@n@Vl@ZxAr@v@N|@BvASx@AzEdA|HdC`A^TeBFKJGLAn@HTDT?~B]NC`Ba@NB@??ABA@Gl@IX@`@Fl@LT@hCB^BdCf@nBb@lBTlCXRNpCcAxB_A~@a@AMBQJKNCRDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C@CDAHAB@@?BER]SYGE",
                },
                [
                    {
                        "duration": 34.9,
                        "points": "lkb@xs_~MJG{@uAY[@UHKTEtAL\\iD`@sD^oDRcBT?j@?vBPxAHbCPjBRbAHxDd@v@JpDb@v@XJc@DYLoBByBJiANg@r@iARa@Nu@HoBLc@FGTMfBm@|@WVONKHKBK?WAYaAkGlBKLMDW@qCCaCHaDhBLAaA?E",
                    },
                    {
                        "duration": 68.98333333333333,
                        "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_B`AGj@CDALU?c@@{BCaCHaDhBLAaA?E",
                    },
                    {
                        "duration": 19.183333333333334,
                        "points": "dtb@n}}}MOq@@M@GHKPM|B^`I~@`@@EKIMu@i@SYEO?QBOJSx@q@b@SpAe@JQdCnAdBf@bB^?VvBp@jAFhANdALPC`AGj@CLMDW@qCCaCHaDhBLAaA?E",
                    },
                    None,
                    {
                        "duration": 17.966666666666665,
                        "points": "jdd@nk}}M@fAiBMI|B@jB?vDAb@OTG@uAFc@DeAOiAM}@Ew@QmAa@?WqCq@w@UgAg@}@g@GJGFy@Xo@Xy@l@OPERAN@NNXVPh@d@JRa@AkC[mC[gAO}AWe@Me@I",
                    },
                    {
                        "duration": 43.43333333333333,
                        "points": "jdd@nk}}M@fAiBMI|B@jB?vDAb@OTG@uAFQ@BVj@dDRvA?\\CTUT[PRPDlAAbA`@FT@d@C\\MXUt@s@ZIR@NFJJDHDN?PI\\UPYFg@TOPA^d@X^b@Vf@Tj@X`@PLLBN@L?\\Oh@W^Oz@g@XW?B?@?DDHLFJ?FC@ABCFVRnAH`@NZHFbAVpBf@|@Np@Ad@cAlExBpAb@jATpB`@R@N?PENMb@mAjA\\lCb@lEdAfDz@~AXnAJtBP\\DNBNHd@z@\\p@BEBANCRDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C@CDAHAB@@?BER]SYGE",
                    },
                ],
                [
                    {
                        "duration": 23.233333333333334,
                        "points": "lkb@xs_~MJG{@uAY[@UHKTEtAL\\iD`@sD^oD\\cCd@YDUB[?_@m@cE}@}EDYAy@F_@^m@n@o@SK]Eu@EOG_Am@iC{AvBQr@KJM@G?OKM[KKCJc@R_AvAZrAT",
                    },
                    {
                        "duration": 75.68333333333334,
                        "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@kAW",
                    },
                    {
                        "duration": 1.2333333333333334,
                        "points": "dtb@n}}}M[uAW_@GC",
                    },
                    {
                        "duration": 17.966666666666665,
                        "points": "jdd@nk}}M@fAiBMI|B@jB?vDAb@OTG@uAFc@DeAOiAM}@Ew@QmAa@?WqCq@w@UgAg@}@g@GJGFy@Xo@Xy@l@OPERAN@NNXVPh@d@JRa@AkC[mC[gAO}AWe@Me@I",
                    },
                    None,
                    {
                        "duration": 48.56666666666667,
                        "points": "hrb@ty}}MkDq@S~@Kb@JBZJFDBNEVQHaDXhEhCb@Jr@D^Lo@n@MPDJDJJRt@PpDx@XHh@ThAv@pBtAjAt@jCnB\\VXVxC~EdAfBn@N~HhCn@T\\Nt@^v@`@~@\\p@Hr@?bBSXAXDZHrDv@zFhBn@Rp@VTJJBR}ABKJKDC^?r@L^AzB]lAY\\IFBF?@A@A@A@C?A?Al@GT@N@TDp@NxB@j@@z@JbE`Ar@HbBRtBVLJ`C}@d@QdBs@^Q\\OAE?C?E@IDKHGPAH@HDrCiBJ?xA`BZd@h@H^?^ERKVUfBeB^O?EBCFEH?B@HMHQBCGKGGGICA",
                    },
                ],
                [
                    {
                        "duration": 43.733333333333334,
                        "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNN@HOTMnFh@xGr@bD\\r@BVEf@I\\MrAs@tEeCl@Uj@Q^GbAVt@QRON_@Rw@PUVIX?rEtAdDbAhAf@HBHQTeBFKJGLAn@HTDT?~B]NC`Ba@NB@?@ABG?Al@IX@`@Fl@LT@hCB^BdCf@nBb@lBTlCXRNpCcAxB_A~@a@AWBGJKNCJ?FDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C?ABCHAD?@@@?BER]SYGE",
                    },
                    {
                        "duration": 34.56666666666667,
                        "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DdDlAb@Jf@@hA?|@Ah@P^Nx@JdC\\p@Tv@^U^IXCLEHe@O_@M[EUBQJSYGE",
                    },
                    {
                        "duration": 48.56666666666667,
                        "points": "dtb@n}}}MVxALXRLjB\\fDb@JLHLFPMJ]VOFy@LO?_Ba@mB_@mA]UG_@^]`@Vj@pFnA`@Nr@^jFnDxDtCTTtA~BjApBp@hAJB`AVbErAjC~@n@Vl@ZxAr@v@N|@BvASx@AzEdA|HdC`A^TeBFKJGLAn@HTDT?~B]NC`Ba@NB@??ABA@Gl@IX@`@Fl@LT@hCB^BdCf@nBb@lBTlCXRNpCcAxB_A~@a@AMBQJKNCRDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C@CDAHAB@@?BER]SYGE",
                    },
                    {
                        "duration": 43.43333333333333,
                        "points": "jdd@nk}}M@fAiBMI|B@jB?vDAb@OTG@uAFQ@BVj@dDRvA?\\CTUT[PRPDlAAbA`@FT@d@C\\MXUt@s@ZIR@NFJJDHDN?PI\\UPYFg@TOPA^d@X^b@Vf@Tj@X`@PLLBN@L?\\Oh@W^Oz@g@XW?B?@?DDHLFJ?FC@ABCFVRnAH`@NZHFbAVpBf@|@Np@Ad@cAlExBpAb@jATpB`@R@N?PENMb@mAjA\\lCb@lEdAfDz@~AXnAJtBP\\DNBNHd@z@\\p@BEBANCRDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C@CDAHAB@@?BER]SYGE",
                    },
                    {
                        "duration": 48.56666666666667,
                        "points": "hrb@ty}}MkDq@S~@Kb@JBZJFDBNEVQHaDXhEhCb@Jr@D^Lo@n@MPDJDJJRt@PpDx@XHh@ThAv@pBtAjAt@jCnB\\VXVxC~EdAfBn@N~HhCn@T\\Nt@^v@`@~@\\p@Hr@?bBSXAXDZHrDv@zFhBn@Rp@VTJJBR}ABKJKDC^?r@L^AzB]lAY\\IFBF?@A@A@A@C?A?Al@GT@N@TDp@NxB@j@@z@JbE`Ar@HbBRtBVLJ`C}@d@QdBs@^Q\\OAE?C?E@IDKHGPAH@HDrCiBJ?xA`BZd@h@H^?^ERKVUfBeB^O?EBCFEH?B@HMHQBCGKGGGICA",
                    },
                    None,
                ],
            ],
        ],
    ]
    travel_date = "2020-08-18T00:00:00"
    travel_schedule = {"start": "0900", "end": "1830"}
    lunch_time = {"start": "1300", "end": "1400"}
    # total_generations = 800
    # population_size = 64
    crossover_probability = 0.33
    mutation_probability = 0.05

    i = 0
    for p in places:
        lenght = len(p)
        total_generations = lenght * 100
        population_size = lenght * lenght
        print(f"total_generations = {total_generations}")
        print(f"population_size = {population_size}")
        ga = GeneticAlgorithm(
            pois=p,
            time_matrix=time_matrix[i],
            travel_date=__format_date(travel_date),
            travel_schedule=travel_schedule,
            lunch_time=lunch_time,
            total_generations=total_generations,
            population_size=population_size,
            mutation_probability=mutation_probability,
            crossover_probability=crossover_probability,
        )
        tour = ga.evolve()
        i = i + 1
    # index, result = next(
    #    (
    #        (index, item)
    #        for index, item in enumerate(tour)
    #        if int(item.get("schedule", {}).get("start", "0").replace(":", ""))
    #        >= 1617
    #    ),
    #    (-1, None),
    # )
    # if index == -1:
    #    pass
    # else:
    #    __finish_tour(tour[0:index + 1 if result["type"] == "poi" else index]], 1617)


def __finish_tour(new_tour, end_tour):
    limit = int(end_tour)
    start_poi = int(
        new_tour[-1].get("schedule", {}).get("start", 0).replace(":", "")
    )
    if start_poi > limit:
        last_route = new_tour[-2]
        new_tour = new_tour[0:-1]
        new_tour[-1]["schedule"]["end"] = last_route["schedule"]["end"]
    else:
        new_tour[-1]["schedule"]["end"] = f"{end_tour[:2]}:{end_tour[2:]}"
    return new_tour
