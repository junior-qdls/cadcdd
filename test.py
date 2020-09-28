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
                "place_id": "ChIJfVNWrIea1ZERE632s71GslY",
                "formatted_address": "Av. de los Shyris, Quito 170135, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.1813713,
                "lng": -78.4842769,
                "name": "Parque La Carolina.",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Avenida de los Shyris, Quito",
                "expected_time": 84,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAH7S-O2M0WsiroMrBboJCJf5mMc1Mo5oCMXl19KB1DM4IveSrH8pbEeAXa_S193GNfamRkDxkg5epR1UHMGNLmyhQMfNfqpokFtAjWyQhp-mouYbfpnzl7YE7WvGTCejKEhB6dkeHI2fJF4s_TMc4L6vpGhTapjEhShbnhUNT5L7ql1vszryUFA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAsF00ComysTNAHjJIZNpqH5ULnbd6z0XLGjDQt4mHSXompUK7MwcZysyMi7ZqTLUL95yDzmQFUK2I4UelBdojDarXyrOlFcwbmTZxSTYiOj9YvQvpLQsQ4y4HtAs1VKX3EhDEE1gt2o8UDXhw-XRtFfhdGhRbUFViejew4z1tr9JZTm5mx0rKOQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAMwnfBr9dRSxHyZtjUnzadl4P1_goQ1LNAhD_B2y1HtItXYw0TI9IUWr4fsNJ03raBenc6o6O5IxVep0W7eryj1VT_b7_3zraYjK6gwr9vzRJMWNeijPhCZXNIFzUQd1JEhCbmP0iQxhgXOciy4lpdc7kGhT8rjOGe-AjM8gQehPBGTvDQ2UmWw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAtjrSuOkiix6l0fz0lWzMQLOQGto7bT6PYeCpG6O7t8WgFrLXl9lfxVbw5XH0M7ev-N-Wjki3k11z407ZIZqjNh2wplNV6hrFt6wKrBhFm_Y5idjbhwVy96Qp4GzUNNGtEhBC6Rp4gzQJ1pkRzac19CnlGhRWWXvuchJyp8bfAoyw_dvb8-FcYw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA1nJTQTr4_LnUYyTL_fPsWDx5XMjWEEQOIOmHcnJGnFh8Dg8ZnQyF-2ItxWITTMv0ZJuijexXLBeb4uSiB60P3132HTVXolLRSn05FjKALGg_HtKFvUU-gzTx9v1eviNzEhDeLG1urwpuq6RceOw48QB2GhQkwDD4O5SCVC6CYPr5wRZ21iYSZg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAdyf2PUznsly7A5PHVf3euS3hmn7jadRtFLxV1Tx_xDL9gJo2sGAW7w2AlFox0Qwl96-vrQNuKQC8Zlt2ziD61vlmxCMrbvSymRpJFnpkuLutdc1b4s7tiAD0_4_oSnNuEhBPe5FZn8VHorLldW1_xPPwGhTEP-ElSGgkxwqWpw_DXXlpnhAZjQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAsosp_5mm7qPOQKpQzQvV8QvY3MezUhJ8YVexaB_Zh-Yolc1Na7BxXjA-jL9CYQssZ44BPWxWfYWVdTMZtBxetoEMUnew593tlJUKbA3k0UxRc-5zQv4t0xAs_XXL7o3JEhB_EMIKJvni-7NU7cwRbSt0GhRAfAfFD9QLSo7EdVL_vaooWnoNZA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAAxkZ5mypbL-V6-Y0y01jJxkiY6YNlfbONWQFoQTJHlJE31kT9L4gatTGZPb2grmItu7kUR4j_zn2-vtfyeQCmT8A6DfswgCF4BW537phV8ImhbjRwh-KEtSPDX1SKonxEhAh9Jx_ylYIL4m_hj7qNN6uGhTdZqicB-9rni3QRQMhZ-NiSnB9qw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAA_H45iEzZT-iKgLpYxXpMEwqF0xKzjQU28R4c8Dh-xd9pJ9-U0nhVgD5oR3ekS8FmUAAvDSzpK_sL0dL86Ne2nb5yWXopV3LYMDR4atIhu-jlx2OiY4ayUrAcNXhfWEjTEhB5ING3CaKS1vASS2HVAX2DGhS0wXspv1GUFrcwJQVClt7ux4koRg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAbXtP4vpmPOPLI0EGNmvFqjWDpMqI-LqDX94gTm9JqYEtFHEP8kGOGA_Hlm78ZNlIpwlcVvy7xca_4Q9w0R57a7wgGNyr5jcaN41ep6NWnNasTHH5I-umgibCNByod0jSEhDyO2fqI3M84GsfBHvluq9eGhTUHkFjN3JBBYvj9X0ZSr6Dcb2lSw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJI9PFfPSa1ZERsa6L1Bhmx0E",
                "formatted_address": "Mañosca N35-86, Quito 170147, Ecuador",
                "formatted_phone_number": "(02) 224-2313",
                "lat": -0.1801565,
                "lng": -78.50046259999999,
                "name": "Parque Arqueológico Rumipamba",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Mañosca N35-86, Quito",
                "expected_time": 63,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAzIcFdn0Rqnm67a2FKmTw7ZBbmg6vyyPA2Tq1AswOq0eLf5XIbxZjFgxdGrehbf95xw8_F-n30OOojIrXjSGonHDOOUahl-Q3srBCSf9D2zcRvK9FjM2ODKf1DH6kF7wgEhDwffWcRSGpUm5lT1F0ZDa3GhTIqRu_SHRCWGRAcGgW7yV6uOKPPg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAecJgk9Zx12zbgMVffBW6WKj5Im5vAaQEg9Ywv9na8xTYAh-PfgZFDVwB3Tl07iQyWjtou5WvOhcLvnKth_hA5E_mxdNj8GOb77VDC8tH3fsgc0-G6KckwGRMRhbXpl9KEhAJYbyc72aAq1uvy2HF_MffGhTnXxLiv-heWc3k2IoRDhYF8V_JzA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAvH7dm7FLx5kyi8UcbUvmr01fjXgkYSu_po-i6BLBU5ydY_c8bZDsIfvKorzx4F-fftsRBj4PZBVpGDSXZddlxUjoJCpNXBag6CsZoWdYCbAsEY6YIhxdLFCinVuKzXw6EhDVQ3OCPXe5sXZV8MmznzCrGhRYDigyA7_RNP-JKLedpvQDpnrBxg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAV0DE5FCJStRbrsI5swo4f9J9zDztEWC-bR5oZU_TiklndkWy5830cjdONpwdPlDbAZ6_O-1nI7KjYs9uA2iX6_St_RbX6Ve4au04H9tc3Mp_lwtzxe5hSlE1uFe-aYyPEhAHCkdHu0U2EWDRSuJQm7ZiGhT4LaAmxr2maxo3OJaYIZ4962VQ3Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA42IivpY2zM1F1lTNZ_65uSnZgs9YiLWsWDkfR68u7-73LDUFrGcQFyT8N2v79wDX7Mrhr2KXe-CTQ5F8P_88Amkh8LyeftXzguopXUTFO0pu9OWmlnHh4hhwioEFqCHJEhBePvLC_T4sLArteo8wMVbbGhS1tzDj2PVq5u-1kRXXsAVnQ91EMg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAwA25PF8aFumAYHpkIUVEs6CNECt3aB4aF6PoqUppknQgnvef2nYeZNHlgCvvlQl9V0JYVhxraNtU2_J-4_XKBx6P5zmLZ22i6e9DEa_2cM9XsvLt2ftpBlyKLtJb0pvhEhAca7KolURkqt2H-bi1kzmHGhSSYA2EZhI5UoGatu6Ft0AQ1ginsg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAQsV7LKbDLmt3SvAI-kf1_RXoqw4lfrqddEtcpYTCyguA87Y-HrsS2yPyv6ljM-o7vszQXwlU8H-reNYAlDR02FFT38rR5vz-TOZDpsYJ7LmA9bzBhxyXR6aQxAJavMZ3EhAFs5AJ0C39VyjPCscmvefvGhTAYx1VlAWkE36JwgYZc5820I8Z4w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAwbsZmam0HX8q6aP5yRUcm_CIWkg1swaK-DTW5x2GGD3uue1Tnbw16xbNDgIyKDWftkV_kVdZVd9LK2fWwXU4RmZdCRjStLAhT1RcZoQGyyCxKVZhINVhyBR2HIwiiGaLEhAQA-1IGP_vqcoL3n9iJ4xaGhTKXa4sKe5SWfGtd_a3ckjKXyOHeA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAMJSbHAGNlnIoX5ovui-JGiru3xWw06LjD78XrqbHNdXtnVRG4cvvWQJiiWn7ojCfmk_6NdDpC0NULIjhPMETVtalFkPBDoi2zqFVzfHHS9mnIsOhv5HGeYCkxcqMrEFhEhBrLET9yFdKw0VYMdJac1KSGhSj8KVtZMjoWxoXdX4M0i0FlO1Mhw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA8MWeDsHOgHnp-aS9OlHSG9leEXtC5Hbx_0dA8MxfM6HYYddX0CHRIQT3X3txyzi8TOo7ekWGg2fh_fWZM0tPFvcz-Qj2J8huHQTVRaf8O1Mn8VHfTutisrsCEZ2frX0gEhCPo1ijkj-zXQHhHSXYk_p3GhS6YufR5Aes0zORN8qcSnUyfDGuKg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
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
                "expected_time": 39,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAujCtlg9KE1CprIPifpemDxzrfAQwUI0qKQIUXxXI9AhtTvS3qb0zmU3pLn-GCeVgJ-DkKJoiHngFF0bm4dpOP80qMB5UmMdksbrMZTPoY89vgZRiVDeI-zM1MjjmsqipEhDIzrBzEy4wiEf9-ERiWe-JGhRguucW7O4WlySYstRrykKkSYCt_A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAFGNzPdkY0t23Rj8IwHAJj5AG1yoAH7xupafAwIDj6ZkNGA7oE-lf-KitKA7ny83AOyevNJD00wFxbSdrxcLl9B-rqHXMQPoxfMhiwktJAfuU7JBPsfT-RdYhl_drM_hsEhD5iWhssnHw5XW-ZZC9LCayGhTpN4xFknFRl_OAoVXC89Mpslfebg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAf6q5PJDePgsnIALd3ZiPdtiuPbxnr-yOlmgUycKr_OYa3JqmBssgwjzE2IIfKLIgqfoAOhl_XWsthOPJd0P48e8S49FzmS1F5f89UaoFK045piVFLyEmL3RWtDj4yOh1EhAO8GVuljRYVnuZ3xd8OTXCGhQ39CzQ4SmMQnYxnHzmHSTHhMX1Og&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAMvAY8YhsBHl67scyWMNa999j-0ryL0fUdoiFxpyG8eUcJplWZepGhLTXQ6BLTDSz-ZoSNohKm8tTlpBLPeBdJjW-2m4csWHrxQQfxVscQ3rC8Wr74N7QybOir90gQqWSEhBSzGRTgelBaL12K3uBACDQGhQz5RsxN-wp4iRD_67-HPiOH33kXA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAmjwVpd83mdEeFxLV6851yYvySHIIaGk9Lkb_F3pqdlLnqDrr3yUaA6oAAMKylBMocZbLBHlHyHgm-irWKEmPI_smWjvgr5q2UK635nAqQB3tk6MtaFknnWHetv9Vp7vTEhDUEi_h0LBb-8dD0mJ1SM7lGhReqFIaqXnZTuRn7Cl29ImW_npJqA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAE0H8gcVUnW2gZQLAHJhmT6QGuXoehCtW06ruN5uaQhUXiCxnU-XaajStGCD50tv-chCqMsGRSEUps8z2d3JkqLCzFXPC_N9zIhGEl4JJneRZdUb9oYQmcccm5E5GkjyuEhBXvBP3wo58RyNarVyNbIkMGhTY-mE4upoyhr6ZA5ZJq8XXykfUnA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAZkU5SlDWDtyS1GX9qex-s4KDMTxUENqTVVL0OtjAEV7i8j36Up1f0dYD-gsonrD_dDfPohFnjXdxF52egHyF0l7w_vq3dU0RlbPqJGqcG3tV2lAiHigHtv-8OBC--2JLEhBh3II-0x6iMaw1e3IN5NHvGhThCuiF-zSjjc65vrQHTf8xpWt0ZA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA4_LOOr-VYt6ANB1SewHalNspD7roDEhWhp_vhV9XaIeuqznrTWnuwAyFN-dKLH4apnP9v-1n2fNML67qxNx0nAeONVRqD2YMwgKTh2csQLJyaAj6l1Qc-cb6Of22No_JEhBEChC3r5QOuJn2DgSQMe-MGhTrGz3KrCaz2--AemfCE4Rr45Wfgw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAoXHKwDLjNVPCo0E0LiQBf0j7kvHFQyK5mmaE_GNrgq3sq0tCXRUTb9AI2oQv6Hm15D1i76K3x9fNX11hbDjBCFmilnaOHqE0BJrHc3p4Cy-EISqFsOq70kbOoXGRWws0EhA-i9NDRbx-S2cBH1nOiXQEGhQp-dIulehNGg05GdvJkZb-pGgujQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAIc-kAHvJSL32yE8cziLtqA0qMTQyxv4FGOj1hD068spSmaBayxr2idfyeRYR0n38J2HVgAAh3AVefu5Ainq3cRHaAiTgfx_HQHaAV0txfs2IEXhAADR9dhZLny1XYyK_EhApiLrBKk3i-7KlVx8jTDjeGhQnDJ3Du_suPXsssZXzhgTrk9wQGQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
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
                "expected_time": 46,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAZJP7NAgWOEF6QD1RpkJA21vrL8lHtol4Jhp6CstI572eTUhlOrZg6RkIOnWGnvQP1y4xPW6w4BKPreHC_Al4kTcoTVtEPNVk9ztrusaRvewHNyFwZ94O7Q-HAbKF_dXFEhDIDhacjWWSVcExlTNpLU-3GhRdVbXXnUN0GvWX70AvRVkaMr0m3Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAxh4RypRaeEA9iDN2TQYYoT0wvE9tJRRP1RzDWibhIhjOGqb1cPbZdfL04XwGJDL0MJ-b8g5HyGkjgQEzSEx59veb8ss6vJ3P-uHHSZadrOeg0efC3LHYIwR4SdgC_m_UEhDy1Hfbv0uiRJhFBnFkNyF7GhSMx1o0ogQC5c4di8Y_3TOMH_GiIQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAY-ebB0oY7NY1ijNik244KG_QfK3YT9wZeGLUmQD8g6CHRASlkUQYjSRjNaQzHk6VgBkoPZ45C8SOnhBsh41l4d5RTsYiwbYpiJz8PI-mfq5SpJH_IqQ_xtKRTYBQy7-zEhCSWMtoo2UymKxh6bhpvJ95GhQZa1rX0Vspm6uzy4Br_sTrix74Yw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA4uxfMbolqv5LY4bY0V_xo0wopVZTAfejpNE74gIPcsqhr8vB66aY1Sxif7I4meyjz0ruVV0W9X39Gf72k1k3gH9NqhL4GkThnE5J9LhRcDut6eopp3-ypIfIehX0kf8mEhAZcMLeHf8o4WnuxzCi8ZvBGhTSPzBhax4G3gyVfltvS5er1_IxSA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAlLenVoZhRxcsugPjoeOsV15V-GuhsIkefA0cRNEEOOpdeQbBHeSPxK_S2NVXBBz8BwBph6OX3Bj16ADE7BR-skx0mzlRkj1-iIy3pGEaXo7dZuPHu8t5nX8tltDzl_0nEhCU7nBPbqpeRymYDHgkq1NUGhRsrVZQvd2uLGyoKJLw2b90JkNjug&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAoO5OqzyuzTpzpBXrq-gdmtTqHmnDRPXaKGO5_j5bXPAQN5STwWhIcVe4zodK8tocVn7u35AO4LrzdkinHcIQK_1wqalskqCW_6tljIChc0DUqxfuAPNSAndDehCwHAw5EhDw58hdpHVU5RzLYsY4zV5ZGhTHo3q277y0o7puRZwQYjyZY622BQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAxfwcp_bG-WRlshLk5jD0lFrd37zE3St3yPLq7seeLc-d3znX54PCfgV5BU4OLcTR2_Jj9tH7BEWnJ3xWE3KxNS702guwh0u2LbpVsK1-63dFU7ATnP63sD76BnLX_5jQEhCUk2kB3yuIxu8CFp83b8E_GhRLhOwN47lRPNozWPVx8KFUd6W3uw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA6vuu22ijT-OcnExbc8C7mkKCpf385t7mlJ_dq2IXVd6r3xQZv-z0eWKUaO0sePf0urIYnGP-AQoXfhhese2BG5Z8O7iLW5TJKYLaapAInJUIWWNGQzERpewi1Nuug6bfEhDFDHRpZVbepBYnasqpanxIGhSvC9me1QvWPReDlkteas1WL9h_4A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAJosr4HT4BSv1wKkNrvSGM4D5j_J-EQ-PUh0u3K_nQz6JOwo4TCTO4gf_ZhgcWgRpJys2cs8zTdUfDaSERN9NkUYLN-rSnk81M8wvD8yVwrLfB7EU2rCkWIjf_nw4A4P_EhDaA90gAzbEfDZkp3qe5VJ4GhQRwLgCWKjCHQI6xIobAxQ94shz1w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA6amlIMjXjrjT199bG2J5z1X3eRUagF1WuurFPnoFuVIszS7ASsk44fNZFo4KI28-cvb_BrU8rt9rx2OxfF282h9xkRSc6y4bL_EvEfWwnmESjjkp0APPE7_BtrrtZtN5EhCkaL-MZvbD84QPYinI9r7wGhTCObvN_A0JzHIKMpwnaT95sYdb7A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
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
                "expected_time": 69,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAsZsrAp7JYOGLFsPOSdNoi0THuRKCi6Md2TBN8t9w-jArmO49VJWby1GFb-TfAb9KiJB8qIdlO2jraVkIQaOKnj9RhaIM5sc_a5T1X_siLlulvCXiejERh0ItMdTsFY01EhBfNRAZ9YB5V0_9ZNMTQuVTGhR_9z6wB4X-_sYQmkv-SJtoPHCycw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAXXOq1YqAbKNXQEPMxYRcC6_CbyIV3tfzxWysWP1QN2LY4F4-97442nxGFxvMp7CVPiZPeLF9hJ_tqnnr_YotSbNJ2z0Zwxjh7FpcV3j7Aw4vfr8IRwD2AB5nTixkBMlDEhDxBmOsJyNOb9G5GDwQMbnMGhTwN0IPOo63_qmFZqkmTt0COIRVXQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAi8GKoHexs03rR8qt-ryaMvW0KZjelx9I6_myOtetslsWsSMTaoTsoChPdefb4rQy6xi_npycg8U-jKlm5pMmJHQ02cPPIfA4iead4K_0Q-q-AIlltqd4RRzrAgc1wivREhDVV5AL7IxOVfZSsAL12AAbGhQoYSHSjs8oSejk50W3qE2q-FaMog&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAEKDwnVO7RFTDhwC3GB0U5POhzSOSQY5gUboUz_q3MlqsYUFnJ-JzNJK25OcuPKH0s6oaMTH2Yfo1-nhIuA683otvW7-87DmThc9lQQAmGP0BXVwOk6e3lvjYB7c-a5lFEhD8Rcr54gT_UdKwCmonlo7PGhQom-qgPrc9LsKCl0IQACDrbsX3_w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAbjW83FkczXBoV4vaSzg0zYmKHBgjsmJzcuQBeNm4qn00j-SDkSd5VvsQGXfOfWbBAuauI3hoKkMH5eIr-XmIcrbVjQDLMfBca7voWkblQ84zziQkaDEaF6pqicVBbkJOEhCVPqFfjFQRSqpfCOIxfxB6GhSDB9EPXXFHWe_RGCgFfPgLHKFFow&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAWDG98zpR7y8fC6aYi_QSCzzOaowbz7sR9E6ilhwnhYpYIj_ywMrha44cMZ-JQp0Ilah-wX9nj-w_rOxDrOdWw5ZM3UHJS4hZjoWwRS9VMnDVQj3MWoUWJeH9zbVcEAI0EhCnAHcRlGW3y3M3nBvZJuVZGhT_A3-y65osEJMD7frYHDYAC2iypQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAeeZ9f3T2j-lypW3bvZyzpBDmH5mjnaXraJgaq24B5dWEBuKSw0OBG0q9WckiCGyH_6FrKQKSxEKfdFWvEIgYg397ajPitPEWcmjTKrZc07z9JhrcixOlIIUsLZvR9FCsEhBsQZSHD8LuTnGxDR1UqvOLGhSDA3Cq_TaOwCH8SOcRnJ7LPOuLdQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAViFVmJtbTfThV4NS48hp9RDIJ7XV32jX_mdNeZwNnj0LT9jPTZgpSII1BS7__ZA-91wQOIoMfRfZ46Vv0_S3X7T5NUJ47-Y8Li2F_2EdxfzvKXTRd6hLGiX_4Yh3Cwm0EhApnjzxufS90gRl-Y3Er1SEGhTCymDHmvdlv5SVdfM86frpwVhWoA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAE4EtVLXh5owY5u6rpY4Dl4PjJAwWg_GVLNwc0H9Wk_AL_Eo6R_ZW6NAXEz5qjt3OKHmoRLK4YWfI1yfycvV5obMlErO4as2jy7tg6zRo_xDihs7T2Oes0aBfHCOx_7ycEhBTWAukVCtZl1NQ-pFxyfPsGhTGZcKSrPLFW4MwXvlOzFb_tuv2Yg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAANjKcy0QitvzeM7PD3XC2KqeXSgf1vlEkOTx3Mkc6sWTWej49sLg0Ev30nn6dcwYPLUMfZMCJAep-emS5lHDYcGKMhEKFWgK7BjzSBcQchIb8R1UJD1iOhaljaiZ9k4CnEhCDw0x99ua25kJj9TKgYooHGhRbBUb_RyNbfgUVlPB3pffFRezJiw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
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
                "expected_time": 81,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAQ7dQlMemiNyvJbFVjJTtgHjNQhlxDzWYLqIIuI831BGDO9Ug0HGUIqcb_gK4o5WbckmWR5AibmBQ7Ns1jQvk70hU-1OM20ghDWbw--J_0CBHV6ps-S1Mwaf1lsTsUTXmEhBviLwGb0SQRJdjf_EI08O6GhS-9k3-YxrCE6eqVTR35KUDKhdUUg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAIwaQ5fChdGAUI8XceA0WkQlCQUwP8LA_tpsXdoxFdOW3dJGdKfJ1gVIwftknt2uwBRxRhQzdnGczhyhtvAWPMBYTw1utoUE3XhergYjVR2at_w_1mOfGbtCgfhQBDuXuEhAqxBFSrKjE03WJeHhPuLtHGhTsGGph5oPyN7cK_aF8xC13SRO2Fg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA1VoNZX-DkNGnCy0ksNN2Spy64x5NaWSS6EcaGOeRWDb6TWk-5c2Hij0efHf2TwfYQbBRuRi-c8m7bper37dRZWHM8cIGVbX88xKWw2sNh3UBuQcpDhxJNFjtdA4hIo3IEhAoj01u9kzlbi90FR56fQ-MGhSMFWhS3sON5dkDfTslFWCY0SOQzA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAQVe-iaRuLyD7ZRAIIHp1YpQZ_YBi7FXX-yTFyEtf5ga69SlCxriK0B2kJA96I1oka_HtEX892IkgqIgdZTfCusN9uE_mZRXYKNzeFdx4ZHS8agb45mFKMmPVi4XyOBqDEhCalAG1RyjA6iw-uDQAD7K5GhR0Lz2xj8rpeYsHwcAKRz77j9s26A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAArWFA07uRhjFLmNxoD1onuJAB1RXQDKlIcf5vElF_DwJPByOwBBkmEuyGIQfr9WgZAmHBVExT7kE2rNrjcCI1-P7_07ACy-dxA6ZDT7TcZSW7074LiuJmyiknZ0NqLf3hEhAemr42a96uBTtvlFipqyL0GhRCjqmLVFs-2ftHJ1NpYV5J4MKU8g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
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
                "expected_time": 68,
                "photos": [],
            },
        ],
        [
            {
                "place_id": "ChIJrXGUIIuZ1ZER3pr6zhCXFlg",
                "formatted_address": "Quito 170136, Ecuador",
                "formatted_phone_number": "099 711 2726",
                "lat": -0.2223173,
                "lng": -78.49909889999999,
                "name": "Parque Itchimbía",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Quito",
                "expected_time": 71,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAc2b7FWrCluMsn6GAm563ldqijEcH-6ud1H3rmt12rM83zGGDLpJCLIWYPqkGsN_-GxDcKsGpPHWFVQqAACY0zh-zy_iub7Dk74GLo3OIEUyWPze1y6stGjFojkI0uSg9EhAW0fXVVzJQGvO8CnCK3ZXcGhSoXvrAAArcMsJ-UBaemO4-anBtSw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAiYycOD98j5UovWzR4w74v27R8W61sFfr8Gfya2ob4AGkZBt7AhVApqnVzDdxMneNLFl-hlRpWNTd89gqQwNghe5zZ_4a-DvyvpVZCsvJ8n8fE95z1QQMdeTY7bOA09CnEhAsQbpjmo38_pGyYOgFv1w4GhRWH9SzEN55q0bF3_jg9T4B_wsKfA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAhfjUMhKNEUIjMFCGlmink3cW0aWpD2GA6DX5uPk4C-0YDDhlpY19sTUV_3IjmUkn1BWWZWLnIyfxJt1RNivHvsGxgOrVjGLHIUpB3_prw_fkwi1JlqwokMs_K6UhWx4LEhCj2zoevjwlzuITwacakBWkGhSHoQCKTIbYQN70I28IBTl9iu_71w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAANlBkR3mdI4RKjT9n75wIbeTzZ0Xz0F-OhwU13hfBqIoddsnANXQMaF7tJyAIqlrfSq6csSdwlvqJHjrmKnqjtf9CYgJOXpXbYt7h5LM2L34OgKu7ZcOHKOm9VDc8HkV0EhCM94wKOXWGzdzb5TpA6o0MGhSt5sLMvgzjkfp9LIZO47xXVyG3Pw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAl0_I7gdxnaGbiamEorcBxBNpL5ZV8XaF2Qwz40RK-Wq3ivp-SqyYN23P9WbIFOTiVcNr0xcIGnG5ar_mnz3rshGDTF9q0KScS6O5GDrt-V7Gz5eS1s9m3HHCZB2tWB7OEhDGGO7M0tqVu3FJY257q2NgGhQg977RoelY1tV9-nDmFejbipB6Cg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAx-YFzh_FsClpz9eRg-wj5h9Zp9F5pV0cWV2oTQJeKnNb5lvKs4HlISOrA9MnSMpSUdMbLgP3SdlaAxl5R3x1UVpJdEmLWTFrPR2FQT_RUB61LSf5JdHGuajYAUsZreHKEhD0Bw_F19OT0XXkMfmo4Wo2GhQsAI2dap80-I55L_RqHNih_4Nt7w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAxy_8He9oPvAODI2ZOKGTpGg7uLAmEjwLbsmjjMBFd0rhx1ljmopijwfi_cYrngdfgWZZ8tC5hYl-_ofupCAddQVv-kSmIWvHJYUWdRKMQxk9G57yUS28mbE1Gw8ZeHPkEhDx90CaqxRE30SQeso5Dwv0GhQGbOEwLVXiEXgzlpFVHxv6YvyoYQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA9Of_PZgRib38dBVrsc53RpCXY6onLYvpmY0VT09-gXX6-UDNgQr2vKAZQE4x5SSHsrDcUuC4S2NzlSNLP0NvXcS8Dm9LAvTg-L1oh8mX0_mtLNLudhJRndAbiskOPLFnEhCdyBiuy1dJG1200taUtCHEGhQo7m_nKNIS_SRJ16YwoZ_wfkI3iw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAGtT3rct0bM5XCnPC_NUuJo5BwkgbUqSmajou21QggmuflGCakq7CXsFTF9ijxDs_cIym04xzY4ZhNQqwbEsdhwa6ix1fuHnBJ-57RvPwNJbzFQp2TnOR9kFJDwwWZBk9EhC-dBeZGkg9fHHRFqfaeuhDGhQ9iSvrL39C8ZstbSyzSlgtfA1eQw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAoijl47RNWsYhRcXLu6zut9JiJHa6xB-bq9_bkkngMCPlrwlKy0zFS4K861KWws4lVnSL1KBbSjFDsBUQivX_AZ1ZcLUFTrOpoWxLEDNm9yds9Xvy6nak9GF-jfh1B1leEhAuWoWyyj88Jh4WG0SuNj1cGhTJNaPtdmn7bbpSG3daaJ0EuyLlhw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJ11Ju5iOa1ZER4qOyQTtGyVk",
                "formatted_address": "Av. Gran Colombia 242, Quito 170136, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.2146667,
                "lng": -78.5024237,
                "name": "Parque La Alameda",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Avenida Gran Colombia 242, Quito",
                "expected_time": 69,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAW-sU4x9eR5OrMi1kQJTJ2qFSISdXk9pkpB6g_mxEzq3GBOqiNhxL6_CpYWzY7AS5kVfl2Q9r84BZGkO7s223p7tbmGlSze_-szkA2lBVo_6KgD1txghgJwuo22w_lQMpEhCmsHYw-v2DY15J-dZ5dvU8GhRPgfOj5C5hoGMEj9ckim-bousqog&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA3drsW3aA57Skt9sBj4pOxcksxRvpIEmxnuWOkY54OTzg7Drc5q3dHlvbPHBOaeocX5ij_UX6l3ztPl2pOC3pmIiHIw5cd7HnI9fQBoyxva0ZkO-l0QTErHfUFkSc6Q50EhAWjIYDgnK6p-deDPSNtU6YGhTUY8e_rcZhGoBVVCYE_tf1dLrpsw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA-bpmBVRbnSHO9OUJT87p-v_k4LgOCmLBdR5X6ZsRYUObJc8yklnl1HoKsDYnA1VXW0ZVIbJIw4aisn6XWMeiRQJgV_Lu8R5c0ARxO_DUU8XW2KSz8ZOB4Owt2vXs65LWEhApvX2kr3y_V3eL8sN988ZbGhTcVcfSxLikh9S9S9vPpH-g6zHKKQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAO3hsRzLUwJFdEd79w6VuLorjmL6qmD9I48Gt_Yhy0AwMKuqQmsAmsQyWHIzI2ijmvrzCFOPmNWbDMR5NMYCmDz8fBH92Ikm7txdudQ3Ce9cPmkMi-7vSqAVCnur0CQ21EhCxZCtRfE9YKflGbHPbUoGIGhRXQbtai0WMQim3iVqkol2oO78fwg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAFxKqJSNHrmjol4X6cwXhFISOsntrMcz1tsQl39PNkQCBnkhPoiexY0wJKAVwQducFKaAOQcw-0Nb5-RLkiuEygvQv2WtU7vUGxZG3LnszcafpesAXyDulYQt5BSN_2GQEhAroO6FOCzaAD-E1hZPdqQqGhS6BI96FDP57SZxSQj0IuIZkGN0SQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAPz0HRvu916OHs8yUgkklucM2lqMqNHbLLkt6TeTC6tbIUz1BaUOm9EBGORg7NmoxYha1vJHPB9RyN6Cjb3GWPNerDXpLelPJOn9iwCoetk0HICkm9AFZoaalP4fwEc_FEhBS8zlwf297M1GqFVs2ipnMGhTB8glNBk7ZRYIHP-CFD7BP8439rA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAACYoL9sJEipfD6Wr1YpnDLFXoIXqLgP1EISwrTazJcsSPbiq3EbYo0mf1oPF6WZTkO3sycwNDUXYDwc1jGaj8dxuD_RMsdoLylzNLHJmCPssM7y2wIl5pgAEMPU4zeTIrEhC-UXDduc7mQUApcNW18Yq4GhRwKi7QlMaXbwLvXgWy-BlVE6Kncg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAApL1zXxxmUoWsoTqm1cgJbi0UJ4ZZ_68aPO_ouEbTKMQYLiS1tDCytxOT3Y6XoT6_1PdIem8p4X0YhYJi_8XXphZ1RQk6QPZQzaB8qaW30qtroIkL9sV0CyX35DbQqeXMEhCWsxJn2QnybhkdDzHlPAE-GhTx-2xCfRKqWe4oly4ExaGF17duKA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAzuJaPO48JSA_uRFNnoN5L2iE9UAMvUcKlp66cUqlQxEyLWwodK-bQwlMFJWzcnnzK-07k9eVTrirbefjme2feKcDYK3RwGlzng52J4met6rDxlys4ZtVF3zTdX9UjiaoEhBBTF5WCGKF4x6kuPJmyLXtGhS2lnEHCgouiNOyDMelGDH1gmZkkA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAA4V_K4Ytmd0rnjnJ9k1ZDT2XrWTCTxHpoxzkjpHK2q9M15jy-OM8Yf2Hw7nxO4FoCwFeRQu_OL51S7pU-LDgqSzFDorZVvuXoz8dY4y2EqadnGD5HR42mu3Uir5eeWLtkEhD9OV0C4_bCAM5ZQHAuQt_zGhRARH2QadZFQxIrTVdpyS70xaD_zg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
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
                "expected_time": 64,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAARxlXQzZzjv_ESfUnjVr-C5DgOqSP7Kc6XiaUxY6mYEqFg-BpH63pQDjxm_ExMs5PYTAmUuvS565zubT5hAAfP3DVqCEVzqERT6HlZzyzgOGMcTI402dKC8_5jSKktiwVEhA5IWnGDxmdSABme_aHbAHQGhQ8QmEz6enTzk0IBWq-hjBcMhJFLA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA4GTBJKieaimfAFIFZ3MfFChrcLThrurrpuyEJ_MprF9j_PASnKbTjR0sKoBEPaQtQu8Lyi3Wl_ykcbR8Xl_59C3HuH4CFZY3RD5X3PqdMV63GSNqkt_JKmOjrsgf4rY-EhCytqHQt-8iPBlz5qye7EuwGhRvUQxwTNX9sX16-i3Y34ibgHR_ew&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAJYMiiFkEgtrBgy4ZJEy5c4c_Dvf1FCLq-ILsxV-qoopnXl41rkWqMEJKn7OGpBdr4Hv2XBEA5JmENHruMWUSApXc8dthWSO_QmfkcX-tEsRrdGW7xpTcq_A91Ir2inqNEhBuymkPMA7m9lYI3EclNWDfGhRQnbaZiqfyUEs8tXSK-BhOER7UTg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAb7HHNzE5xxYi2PNe822XYldw3Qb-GZdVaxBqQTOQLRR0hXOYIH85z3oi1w0C7yi_mdU1fGQRymlU4isLh8FELCQj1WYTEdRgHuGU6lekhBcLrW3z3uL6vuzq5q5_3YmJEhBnMnbDiplMzMAH3PEaMrVKGhQ49ptA9T0DtykWqVIsj4KR94upqg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAACR05QUZtsqiLq1K5kP1aXuHk3jrcnQmy1i_I2ZCDmAftWQ8uzepsB5FVZAiY7vCCCjA8Bv_T6-TB7bptl0eovC8vL6gYAVGILmqDaLqGPMFXm0wyCwBZBtycvshG0R_LEhAnMGwrwcTYvxUccW1ILJKHGhSL858LZKIQEOJZCQuZm8d4WNBNPg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAIY3wKCkTxH0k8Q9tC_R7K3mlYdrqHzkZXRrexuxhgD1DpNsOma7bRNFFS2cGshxGrBja9zvK9tnVchpgT3xbcaC95AxB89SjFjIcoSQxLMy-9v2QnKQaI9eJOH1uBRHKEhA4l9fVw-vKpulLYow34DwsGhScK1rh9IYXj9E7bxxa4VB-PM2Zgw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAUp8NBXzFT8wLSKVFc6TUNoDNL6eeWiUHrQ3F3hXzeL4jHfjmcDaUR6fJyYflVtseh34bpwyVs-qSZj3K1OY88hmvNOSeUUtUHFjkoBWPYPcbVX8UVg_aRGL_9ZMdYqvwEhBf1ms90pdsVuuwQIqzjkvIGhSRm0FNS7ZcXXkI-EQD3v5CShHJ3g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA6MdXNc4u1ZxqCAyzlyKNkO_wKMsVVZ5pBaIclsBXJCeNlHvEQcZfx-HzbXLNNyWVw32JTk_ve9XAlrEHU5BBZGwJibpJaS1YiUBJRCtSYBLnHicB3_xSGJbMPlb4UDUuEhDeuoua0sanBgc8FeFxe5o_GhQTD9B7UsSzrF6utAmRW_ruvhRs-w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAycHWI_Sd9y7MgTAyl1U0NeMon-CaV1r_Va1QXIKDrJ9YcZ4aCG5DJzKLJmB0bW8MSBk-sUxx0YLwaRgCM1X42F-jVPRMqiyjdwOiMgICFllUG5iRHj1NOnhi1DPHuc5REhAFSEQN_T3UHobloLlHqPRJGhRfxaDniEAVRUMQfn7kTRqyH14brw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAisXN4Rp-MabERzzUWbH6fBGvQfwM9WuJtcMoo_sD-xsw2DCwaU474uF_hpL8AgLhKakZEh9gbdUhl49kPA7k4ShGNmm-JuCBDtI8pCC2_MfNUwTYnW-d_-ksthcKsQV4EhASpMSulpZOZig5ZuDdJXCEGhRZRCNWvDusQ12jh2W4hGV0nOjTAQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJGzMVUOaZ1ZERVm6Rtu2bV0s",
                "formatted_address": "Autopista Gral. Rumiñahui, Quito 170145, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.229867,
                "lng": -78.48575509999999,
                "name": "Parque Cuscungo",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Autopista General Rumiñahui, Quito",
                "expected_time": 69,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA2sr1os73Omh9UkOBRpRaC7THa640pRPbji99kGmFZ_4BAYyE77AujjZgzup-tK3QCp8vPrTvOJ6v08T5Tq3zFQOsaD2eBXFVgBzWt4BRFPa003pvaS47ALaQJYyQqhuREhDBIu3aZ7mxAHQHcBnnuafeGhQOAYC59NkWw3vFisuH_Qj3UmI2zA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAwCABHqjjSS6OLE7Iyt9ZlJdNfFoN0DXN6aRad7YOrjo50xVr2M7Vt_E_iUHulH3n_rYiFamGjYv2X1iHNN0FafOrGD07kTndYOelfAQJNZfIKH44-085Xs74qwLrdGdyEhAuDodIu2CWHpDvoWNIUaJ-GhSh07P4qehqzYFTc4bORfCPfeHidA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAeEO99uNeB_v3bEfh0qxj5Offw4L6IWx2rRy4PQbaZbvKTHMojNeCzTCAz0GQbKlxkWutFrHQMcfX6vUoSHDwsik73qced98wisw-zcdrvjBcpfHjHPEvrgysYe_tpL1KEhC_ZT0U1ffK9N2TjplTjMa_GhRY1RJE6HXgglSCoVfbXC781i9N7Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAlvBqpuvmaGEeVLPViwlcuYBvvFHV7U-t-7xHb0UykM_Ehi-FXCiRIWx8UQdZssGfbim8uMZ8I77cUOlPXrPbyT91bF5Ie3L2uyUcp8boYtO3vRSC-4PpZMm_1DrE32o0EhC6yuifDag2nNm24N11EPJQGhRwDeVxNP_i1fjvPcKHoXjvNU9r-g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAATRpRiYNjlfOlVsRjCBqLslave_2hMfyxB4AKLlF2r9jzXqP1Ih_glo_nDXv3dh_hNrlxE76kc5RTJ3b7NteXNGzupXlQtRt5q_5DMq22Zk9R-xDYV2PyLmVoXjCPCSKoEhDLhSGc0TZJ3ZzbAmoqDnMpGhRbw7a1Y34kgbIuQVPkUM0H1mYL-w&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAM3qapnszGXv7sqVfR4UnZY0_jkUcTPiEdVz0Sl7mtGhDqME33dWV1xqXU8CwAy8CtYhLcqTZjnf-W45heoSifLgxe6mfiuoIFT2Tn4VvPRcwCHPnzknzUHQqmbbQOxCFEhBZhROdZPp6NfsLEeIfFdTHGhQ7g1NzEClztQixR32QCmiTgrTrKQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAmZkuLSzkUA2bZTj5lNY17mnbxwParqyMhN_mx7nqU6YCRE-8QUmEa8WfqocI2C_lFF0DDGxZEg8Qybjt9sdmQwcPfW3mM_AzH6-sDeKGFC0OXrq2fxDY26qPPMBpBQPAEhDGMLTzsO7HG_oC4itwpx4uGhQx1rbxszlPRtu_wQOhoq6xbgYPAQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAq82I9vjJfXYEEZ1NLQJlKIl9B-NTYAA-2cXVzcYmsfAiL5TPhkGwNv_jX1hxGERioGkyFcwpMwuAkl2W7m3S6jiTKqZUmeEMo0j0R4-8XO80MdGH-_BcTR7yXKbvJi41EhBGogtt1CUMFTH-_sn2nxbCGhSrP2JDoq2UUzixcN2gD3vZJWf1mA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA-L8WqtlI3KMGgeKAA-ecW0lwjhqQp02zHte-3yDMMGdSfkZT46G0_HAaMrwtapaTmuRXu4g0bhCQ030YuX0AUpNPZNn8T9lEtpsV_GCKaohdEsflyW2xOXVCRUKo_rrqEhBFZ3Gf1O_nNiYo58-ZE09TGhSkVeeNh-MLDBHbbB8MjHimeOemCw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAN6ngNq8PDhlUe4f7aYUm5HNChWwBZKdr2YEPuIS9O0EbYMOlJjgT9uAZlIPPZU1rQXOMUsw1yST7ybVbX9hfrxuGoL_Mudhr4nAv1TBa8HvKpTzSNnK_4Va7g5Lu5axeEhBh1HoWNh_EzUD7bN5lQ2PHGhTd3uvyDNPsGzrbLogRMUzZ7tmWTw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJUYOujBya1ZERqdYIn7sxVcw",
                "formatted_address": "Luis Godin, Quito 170136, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.2164616,
                "lng": -78.4891136,
                "name": "Parque barrial",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Luis Godin, Quito",
                "expected_time": 52,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAVMWdJN3w8VY3WDPpPSPiqZCujzbQmvAePNfMguNKlbSOMOmIC2TGkRmAvKAgXbBYBonIXvG1IeOzfyJ6lqkiQ__aQnPjAMc_A7FO-YJH5p3VM0ConbO8Wx1tjkY-2CkREhCca3KXKBkE2VH-RlkeL1P8GhQ-oRiPI5LjQG25WE5F057xtrC8yg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAK01KMpPjLKCiA9fFgXNXCOj7CKpzYIZIqQy1ekiDkGz-R5VNTZ_DzhUn5od2nh6koPqEGXJE9nsglVmBbaNdnEG8NTqB4hq5qBFa50TYj18XYG03AVWkr-GIwoj5wGuEEhClLstlYoSLtnVu56G6lao0GhQbZ9vVXaFjCtF2BT5OXs1WaGQwiA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAPN0Yjjj3a3MdMZ6H2XY8KVbtPGlqAFGz9tKITujexEauAf8mJ6ba4ElxDHEHm7rT_y5p6uPbNuDlWL2Gu_bKyaGIYAGUsS7W6uTeS0axxyvUic7Cyz87XUewj9OtobPhEhDVWb51CUg8WoRXiYwpIZtJGhQZjnEu6r5jkp0N-wH4zjAq_-M8Xw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAUmly5YKXY9IR-ndnN4BUDLKGAmUK1eKaREbiSjzdtTcq9_ez3oas8uq7gDs47BzDKRnFai1SL6kBBAbn6YsIjFvEpTWezweKWkJezQFSsrgzV-LhRHhAxjzOC1o8XGotEhA0Ot1eiU_w_ZCWu3qQcSA6GhRjLFL9171ykFIrKvpl-NtvCcl1Pw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAKRsCNQMamR7CxVm9c-2pt52CLNUXRvS7MORaJfH2fYRL9Ecy0YIRZQkF47L0qdcRuuVD0fE0HoVm9Ty2aW4xLspxGZwgljjrPYAG_eEGyutBkedq-vXehM1DYUXIRKr3EhDSmY6Exo51slpT3HjNWHcaGhTjFSevWzH18lxTecaW9YL8u2epzg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAbY9jep5OTY_yhm1C0iTsMjGE3dhIOZz-HXDBsOAl194qIHTTDwWxZuwjsQ_2gqYzCxq9RX3if7IktU551yHFrR0yc1Ubw27uKvELUDkW_eF5TJacVye5MfBHoChw7mDiEhCPNUcmG9K4i9QOTiXfpdkvGhTUF_1brZlwO1akbMLmZv7HhX-dOA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAfszKPPWw96beXrM1eX9EPyY17TyCZMNSFDXeIu0WnFeXbhF1jcyTSpWw6nzX1xeGAJqreAaHCB1NkvkM3MYm6QdhbGhTCELab_uS-ooNwW67cAnvLeXrI3M-whGI8pw8EhC9__VhRulnviBYisk3aKXpGhSSaJBLYOFSRVGE1ugMN0qI-L6Pkw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAsIX7NVGyFEpB2qgN9SOqHS9S9Ax0-9IzG6mfN9oKiHyuZvCo2sABDr-EAqj0Ym-OuRwm4VjTyMw4WldybBSrhVQlObdlq56jWzh4TUyxpGgLPqT209ori0YCZUCpQeubEhDnbNTBlcXReWZNbIezxm-rGhSAWSohRQDXwcIrBW8PGEG7tvuvrg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA6zxwHhHvRJVimHzfQbIr79wDA5Ubjhb-zKoQcako7P5fwvlD_fn-oNvR2IH97yQgc9Hyv7NA6ZPb4fILbNool6wcFBH-sx5ATydhIg0YskIpvPfrTAt_LZZkvCQ65yAwEhCXdhwg552bkOANOCI71pR7GhQkQZ9Whbsnem9kvJGjGYu3E-wFTA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAnD1g21WW-GsHatKRtfufCfkuYZLrX9BDp6on3MIOTG4z9bEj8brvAy7_9m75hmDrgvN1c3whxg_qDEH97L9pyvONeGZGpW2SQBDSPBrvL0-KxBfR7UQXlpfQJN8p_92ZEhDvhfuPH1dwBCl7j3oPDV-3GhS_O4hBa8zA4eOziP1O1Gb-n0ZK5Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJ_2eWV5CZ1ZERFMbTqxeENfA",
                "formatted_address": "Piedra, Quito 170121, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.231169,
                "lng": -78.5060922,
                "name": "Parque El Sena",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Piedra, Quito",
                "expected_time": 58,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAzJPW-SiE6KNlNMtXaldpdWXMMXWAuYFoq2snPF7eq1kMgjew0oaAbtiE1AzB2LM12pJWMekrjGtK-0zJEg8fMEiSLvNyo5bhMPpehpTQz7FanQ9prPB0LsTTCXOthn-2EhArGcHui8PEWaj36rZbS6p6GhQdvN0DptVrJ24K5X1ysrxd5fhkSA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAPl7d8cgbyQOAyjyeDJWTywLVDTt-x75pSJF6_75Ur9UAFke4Y8h8S4Q-sS2fHjhW62C8kbXlEhdfQJt-IzhJTMShCWjWenTQJDQhTfTybe5i7TnWoZqdS_j8XGA1j9KvEhBJbXpJADCUpShwxUXUA6wiGhRg6znswMVNBW0ve8ruHAhrSFwFgw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAzid-FHRD89m6lbNICqKsuq_p3Vh-vo22MLAVsKk9ptEbqytFe0_hgE7gEXaM-35iJj0qOV2nbdPCFDq3KDRjeGPUO6SKE7RJ1wMiITWYE74DyPmuoSVPRA8WaXymmUU1EhC-y_IxWZ7CCNiJg79eJbAsGhSoVL96KnYLMjSThgUzQ3-LC0vNLA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAARqWdcU6g0GFNC7lfWNNpF3V2Qgo_8wCUocyyBChjhmRB-x-XfW5yjQZahfD81O64ibygbjNovG35cIaO9oGq1pzpH3VHIDK0XQPZrXQD7oL6G9hfz7piprrTzshXm-vpEhC6y3kfhM_eQJ7BnW-hwRABGhSlhcV4YKN9VhRw3Zo7NtPRV96flg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA7vON1zq5poC0gKlRZ2J8jCdw_zZcs3EWcoYWx-nXbptgFGL_Nm7ICBGvw8s_6UfDITud1ORYR14g-afxI4uf0Tzi02bhqP94zoShVL62scsC9Q1pcCxO_27ho9a0Jh0nEhAyuxNMYSVZRLVxrSIK93SrGhTmYZ09Oe-hGvWKVABVDkZZnE8w6g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAeNCySw8PSJKa0rYcZmjz1R-hQ7DZ_wDQD_id6Dt7pW-FaeGBMH5ArUFlJzG8A-9HRfALBmO5cFxXXvaD8ngFjF-sCvWiOe-M3KuN2arElslp0BEB9zbxHiTeLgAPzKsrEhB6ir0NnTyUGiDDAbwyRI98GhTtKIbBN2Wqn6ThjQQEaGcvhl427Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAui33qByvxRU1paHpkLqIlhV3YI3VawEMdSZNTkQMDQdhY7zXkmfeILkl-YhCZo0Jw-H7PCgpJ-BvGlgUOX__zBwPa0q5Z1vR5gMIHLPHdGmuePqp9M437O1A5Wk6QzktEhD2HhhlL7q91K1BoeRep7M5GhRa4ys7veE1rk6b6DVMyAzi1-oVDw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA2A8hXPRo8ym7XxGo4SUJU50QoJnAeciio-gfkUg-elnspu3XqNbU93T_SE33dlQA0EBL99Rj8JUEH9SpulqbKbElWacKOufYk67VLwLdfKRvh5AHh2Ab-teo6Bg08XcqEhCiDpYaYNCwbhmIj6IoyT__GhQrlmXyxUod6t-xjNAKWbYS9Wv6ww&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAafxwvX5Ja5nAPl_j-ZoZ3CXLGBhy6Wfrxmu0EVDq1ketKHMumLrja9AfYg_NWdlqJ3zUDjiokLZl0gCaFseTsFrFUkoAN0I8FKWaJKo3N6ZROW5tpiUvC6_5eCrVJTXdEhBMYzJne4cU8yGbbQJdCf9YGhSbNLWg7XS59HHKNNAyIv3UPQPbFw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAArXeVUZXJ1fwTDsc734jGNKq7VBS1As_9FBl8bWHqXR-K1MmRpjKBS1ksxUfciU6enD-UHJIAhYHw2ykOpsan2shsDZssoFFkN1FIdW3rc7KdDrRVCZp8MoRDlvy0124vEhDqzjEgOfDEYNNKRyhfOdxEGhTyBLuu30kFCQ02xwTLHoZifIN9AQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJXdIw846Z1ZERPxQ9GiSpEK0",
                "formatted_address": "Calle, Ramon Miño S/N, Quito 170136, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.2264807,
                "lng": -78.5050626,
                "name": "Parque La Tola",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Calle, Ramon Miño S/N, Quito",
                "expected_time": 47,
                "photos": [],
            },
        ],
        [
            {
                "place_id": "ChIJOz3LWEiR1ZERVjbhTba9oFI",
                "formatted_address": "Quito, 170157, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.1963792,
                "lng": -78.4731947,
                "name": "Parque Guápulo",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Guápulo, Quito",
                "expected_time": 32,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAaGWiZGqn8DGa54b9sqjxRpDxt-7oh4ixtYi1lHyBjwBxxPUWg7dp3yyhy7sLJSuZ9OWzIocq1m19zesYjRUqpuOM_S1kdjL9KwxVZH3DyNYCFAe3zsIKuY_xyR138Ee-EhBqF0yYhjEBILJuKpLtAGRGGhSsYKdHi9ytJCsVSzPeY4TRC0cIag&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAKqFs6KJWy4rVvgKa4Y1O9PrhaFIKockHaLeawmd7K74RgGawTSIzpt2OVqUp2dlQtWq2ySSDKDhRMpRuy-x_IYTZhMWaMBxm1cgKXI8z5QyU1DGkgJm8LNgEjqkaFJFREhCtp8UEEbVz-S6yZ2o_iO-7GhTJuP8hIBdhGO63PHvwu15PsmteTg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAATGNAXniXbY_TAucBKqM-aYQVtfDbBqFfHKtY10DnLwmQJdRz_NPuM5_b_OTsatpyeaqSlzlaeSBTZWTR1d9hLKsC4hea8Ba5D3rsINgtfSOpqnOKoiCc1U6oLBgD751bEhCffMiKqW2yzyBDlDU-VY5PGhTYRNfzeliwl1OoHexkxnghm6fbJw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAgU6HfDDJfzorRe9V6so4DRFSS2NjOpjMRrHk2VH-hbTz1UsXlqwArtr8tDoq9kVC4Qs5oGnpySQF4A3TxlCpVkWrb0289yXjuGpbLYwZXOiBeuBa5FkI72_fTyUCGan4EhCKFiRc2nnLvLIOgOtfZBD4GhSqcjqqub8XjnyLl6KU2i7OZCQbIw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAR60GWWpB77OkAs62KbmMul7g8I7pfh1LllYG2ozL0NiOGcEY21CQdeK9mEcqYWuRp8sJEy1dSyl2fi1YliOpz1HT4agmLQXje2aQuFaPMMi3KTl6feA-7zSpBWxxgoq1EhCskJQxQwijmkRydGx7ibXdGhQqNX-G9kRKj4STB_KKnRUY2HemxQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAm7mS09zrJWNmBAsn2PyaXlcIyppoY7ux1o2hQf-eu4XGOpmww5FKg8J54c8bSa5sCclT410SgoeThl5Vz1si1ah4MNuQzfqa-G5IdAxQ0_DoZNpDoWnqYDnoj2IKJCYnEhC7-GlGlqCcFQm3HAUS60xPGhTxJ3NA-3v2CIHv_uf_9HTSkD_aqQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA1RE6KNqWTqBujmXDm4y0ZmuhKem18K2i0KyW8_0hAHwMr0BDxC53KQX4aUdg6kkJ5eOp_6s9Mrkn-C2HbbwxWCXF2Hn3CC-ipSa8oW6u_rim7Aj2epqZZDrHwq1sy2PUEhABg-jhJUtW5o5hAWIfz21MGhQOfXEzylj6Bymi-1UiGl0YmeGDQw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA8ATP_Yepg2Re0OvKDRuZsLXBfMLtYw4Z-kn1oknSDWbxcIIC2OXBL7_qa1Ic_rTGD6T2mr0-Di9fHByE3czS2scVpZOzvN6TequRqJRTxmL4xT0EquRAx7PmwCCopKkjEhDsRw81t5BY22rkO36PU9MPGhQ7DHG3wfESJPlE9TY62UaO40IpHg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAcnIYw6Fte09bBPfi7VYKGcS8OXvgc0hixpi0gVSRQNa9rvMDzdrJb7dwcBzOTtLIrcACt74eK_NpkVRBIuZXCovzJ6vqniyzO9a4p-JfPXAUGbEq08ILk38kYiM5Jr9tEhAoIRC0A_R2HbHIqcETXfe5GhTAH_Cc9snWiFyT8tQV5X2HrynzIA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAwZPbM-lO6i99Pk5o9SJmatGQWA1TeXrpHpolgDcoxz0rRtPEPxu_pPTD67qA_ss5U2mRPr90AXoRm2iSP1hYfh9aZTfSJVTq2W5xiMUX_g0dUzu576GxWlx_R8CK6a9_EhB86-CWK1adbalZLHg4EZIUGhRdmUveL8Cw992DjM2IhdZceSKqFQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
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
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAW19k75DHhox_Xv6Yod9NwjD21a7ia7MYsJKu_t4C_swbqJZ7e-8Rm9E56BPECjzEecUQqeDC1E2ZAtgR7Myiho3XqggiOP3q_8Cs7v5F7-tO517ueqLNPNWS1n14mrwaEhAghMW-sD9_wkCzeP7oeSt2GhQa8IuC83kqK9G7R0V_4Fk9SJrkDQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAGCBIyDFhEVMh5dDpCyBw6O6qQGNyrjC3O7NgX1nPWe7P6AR9R8WNTxmJ61l5XW0mIQuq00cO3S5QTbHC8z8AZz4gbyE_A358WnCbcadbZGhIbNrvplK-OvQMT8JWkDGYEhCwALJhSFLw7oA7YTlsb4G_GhSgsWReZu5wGizpVk1mpzkgwlMJcQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAq_Qri_eYJf1UjIfy_wu_qx3-1CeQtay3uxhyqkJj4AcM66md63Xh9GZ1WhYkqH2VlUtEnEDFqEmXw4HZeQBw3nCPy68SYjYmBonYHs0bZljeK74d9uihNFAim7l0KHbvEhCBDYAF2Y6WkcJfNyBCDT1cGhQCCzdjRq6kX9qVu_blMfA3QgOOtQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA_T68OipwKYh1gKax2zfFVNZVsLCKTYldQ46SGaAWaRSTOBRDr09O84pAVgBql3ZAlgn1LR88Bx5koZWfnbUM_fexnyefuBSgsMLoGXUJvhPhoE-sxsb0NHSNJXBKr8DvEhAcLZPspGMG8c6FGD3Vjw5zGhTNcFCnNkZrctm1sVxx5PDvmK08Fw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAJlClgn1xrVZnQu8yjEA_EtMbPTWZTm6mBj8-_sslR6muA4yTY2rBH4X98CXpAmHnkd8GzvByptdNSX6OZJbpwZVVgkNwVBjKD4FrXvhhQ-F_tViCY0R1yUkOmnlZw1q6EhDq2EtBYXUkbowSTeMEeRQvGhTx6TXLtJp70eluEMcHgfYYdKefXA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAj_1Eertel7ZJylaqfKf_PhcrZl9z7j2D1TnZr-ar4cG_ZfATtDoKbO2gkWEarjsq1GQeft1WeTdzjszRTDwnP-z0ytsQigltYRFRUM-Gps9jCxw1awhBeHfIi56R4LATEhAT3RWYXTf2I3pU9zTzCMVzGhTSDZvHBDA4ySjrOJIn-qM-h6IfDg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAsHo5twWCjcCD97apmwUR7Tje6bhOR-3rWq7PSFzHQWZfqnPojWXEtzKZcQULhowVMTLe3D6FXknzvhrSbueex5C9epwktOQaUKjC-lE4C3WqjV6fgxtzqaV0Tntf-hcsEhBX9zX-cWCygJXpXvbGDVOPGhTk69bjEeZv2l-ZO4E7sUJTH5KtjA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAG1rGbEhkoNajxlLAel9j-fd4gZ0Q2s-7ZYF2pIRzkIV8E3bnUUtGN3w_bOt3DY-J5z8zdL_GvBGvX2lEMDXmcIm6zhhSx5wwbmeVYL0XDVkGCwD9LK0iJn6o8C1U9klJEhBWvTV4pzoR1lfkt1E3YD5dGhRfmzLlDNS9pVIQQnqPwe-codJTOA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAvBDJJgSF6Vj5N5Y7NOkAdLl4_M2UAFaSAhB2NCik4zAuQaNpndcHk_acM0Ck53MDrxe_wuls4IlY57ZmjBB2e1SMbjAWbw2OMI0A0krL57JEG-gLKmpg75UQUvTt5y-0EhA123FLn35WmLGXIRBrY7fIGhRyYOCLCaFf-FkTPAEQutJTfX9X-A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAY4rn4Xode6Q2TctY32eO_Jfu5ts2AmMrTrfeI4A0JXfsbyxtfhanf_Q4_avTspYC_yIaPNZBbOGlMAK8ru6eExxR1EjVhYTenNNvqXeKZODTgDkfOrD9l2GZOS3XEnAREhBuqryDcSNsj2pA4OlSDo9mGhTEgWuFDJOZ7OO9DzjLs8YRzdAiKQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
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
                "expected_time": 49,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAANpW4Pn-83stVWmOwG8fnE52GlC8jMmgOsQYGc3ud8M0gBHIHulzCdo-zc0vCl1NE1WIpU6DU9Ta-rnxx7i6Hcp1ktskZNbFiw6nUKkM7JGSJ8OIRQ5oFzU0HIlf3dyiYEhCaZ7qTPf5-m0koDCZy2xY5GhRTote1bwfsXHTne4kfQiHETpCxyQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAl37T_pbjl2JIL0l-os-aiV8DyWwUB4fgzSg9aZ7iQUOYZqgkS6tEEXIF4UzLs94nNzraUoZuO2p77x6WVEz7aUQ5Jx7gM70ryUS7LK5qAID6R1ZT-twdolFy9Vfku7WxEhBdjni9-dURF22mZ3zZF6VTGhQRF5Xiz-Uov4hB9_LE6otQgCfY4Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA18vemXDgfhki5fD2C79X0k4RTxWWGys9tmyZW1Dg2Y7k-PyXz-_cHiyXjwU8HaEQ2HGiXCO_K9VnxI16xZ_7wcYNPEjNMrl3mp46jObwwiZGOa-383z-hhLaPV5M3SmMEhCbkR3ttL1ouOyMj532UpwmGhTVnxSkxNGHgM9w6-lS4zqPQDyX2g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAThq0qC8Faj92clDXHQ-6GPgxFcgM9jtKHXnxXyDrXbu5Lk_tkdwJp7OMuKLGNZl0Uu-Hq-6Ost8J0811B6lmlhqlhSKqllkvi1CAIykYXRAINK-_e4swXPOdzfQ5URR7EhDfn4c2CXiyWIs3JI268rJDGhRVPMT1l1pjnE5rh6_Xn0EzQ1IM6A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAMXB5E3sphUtP4DUGCK1Hti9XXEvK-OTI_mWAwDvzFg9kgUiWyM3Fo-60XNT8JfCyV8Jq9C5fKWRG6i0HGdd3bx3shcPSmParpDJat3HLR2QnkCB6VhBFXerbEUdXHNhXEhCASUzsAVliylUiQCWqLNPnGhSR83bWFj7Y5_V86Mv22LZ1m3Ektg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAPYCmAYMgD6xly37suuBkZ4XUNNFnelzAZQI-qIAjAf39zUgLL8u_GE_hjSoGLb-Vl6vgZLayaXu2aB7X8v2dzO3ptSwYlmiGjaGdGzIs1UTPNlX3Uw6X5bs1IZCftIZCEhBvT6slO1pxMuYG0MmUBqUlGhTkxJCIeAYHxMoX7lRbzKXSJLi68A&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA4BX1GMfzY3phyO-ZA9wbr2l2VK4QxgHRFb2fvyNNI3GgFlYDx1BvhZU3qr1uBuxSSmHnEI1hLSd2iZDklS2VtvNkY7E5_f0uy6sqOkIFfLQAZPG7qf3o-wTDPD-ls98jEhCE0EUkzkgm95CDB-CNOMJFGhQILCehmIdLFMFABf1U1Nr2xLZ1xg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAkwlsiZo-E3sEy2d0FA6uaB--rzY6SalgiKS5fw1DZk6YbXiTOeezST2DjMgZwlcYtBEZfccGzCvcy5B-CoXQoybS1LuYyk7hSisUyXQVRPmsQG_2S93j9vckD8VvjufXEhBZ_hd7adSK6M4FdoTvs8TUGhTHDqcOjntXUhNxE-1g_SP5FYXJMQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAKM3db9Amz8lRIxJvdbbYo3UOKX5pYzMDrhRuki6swHMDcDjPTyvStDXE8W9G0uOYc_NbeGGJ-Zs6PCt5DDM93KoD6sDcxbxoArTJqq6CR2Za8rnPN0hjadikeKObV7tFEhBDrugEJCxKSsfNJBMAvLeYGhQBQPlR58-9HzgXvkY9qIw-Lzf1ow&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA_MRYpAr88RX69UjsO2fQGjrpH9UyYcISoKJwMfhIXbyGkXbx530k_InAK_RCsx9rMpcXdrnzMadJjsY_hWW9P_Hb2lnvzqRFogaLoWf5IlHmJQC5Ig_cu2fozpHKOwpmEhBBA6lXDVOfQMPv5bEhhm5QGhRpU5fxZK7hAlTi7pNexUqAAg1_2g&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
            },
            {
                "place_id": "ChIJE3Ioinua1ZER70gk0EGwWGg",
                "formatted_address": "Av. de los Shyris N35-174, Quito 170135, Ecuador",
                "formatted_phone_number": None,
                "lat": -0.1847318,
                "lng": -78.48486299999999,
                "name": "Parque La Carolina",
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
                "vicinity": "Avenida de los Shyris N35-174, Quito",
                "expected_time": 71,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAY86vzv9y_yMaUlpItFwe983kvKa_ABQiP2l9SZqcRKcigUmzxELtc8u7PPpCMyW_bpQgNUHnRz_ACcjhl5yLmpxHRjg99BseQzJwL1IUENXeMoEU-9NodljwsmySkoOmEhD_WqCuRNlHzo_O_zH20-4HGhT2xr_QuNpfjjaaNfv2bFeFpucxsQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAWB9QlvWZnbg8TDJXfmQhQSDMVAEsSMggFqNExPChs8VZRdQGF_rjpdgFt6arOKJ4yLq0h9vWPQ2WKC8Zkf3Wcris0JlLhEmvY4iPy3g28Q3JmPRPWud2vkXX-2OAtgD0EhCTe7fOao1LtLBVvzsWHN4DGhTJeQo_XbPVVYE8-W4m9py4AADmjw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAFaY0xpIfseL7UdfHDmf1a8So84HWv9AGgmGpBF3lgDIyqzhCSJjK2MMZK0_qrA898IwV8EuIPd_Cuap01RntQSRTwEPc6pXo1vwgP1OZd3RNfC09932GB9F7JUoSpEyTEhCJkva1oqM9YHSsnF2nZTIqGhQEN73Eo6vFmYvhV3FDd4RUS1cZ4Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAFwpKS_-i6RgHqtNHb4G6_KcToWMyVnP_uW-NPd-SGJG6gflpupHIsLqvweL5gv8p6m0jdsZPzHHinezm2mfiJvt_R148GJCWHekblN4hSXPaQbUSBo-iyaCwu5RMWrXTEhDul32kyD4fxIKWAwN8mrKgGhSPmmagIHx_W46RaJgrYtjk960enQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAMlhXM_s302bGIP9uqgEQpAfKYah22jAr0iDleaIrEJ1GZvoQ-g_9Rt6pQI2Slig1MJJkHw41KS4ZX_1keo-IHzXC6DtmmdE8qo47X_FGxbnA3zbuRYBdj86Q1ghlT3aOEhDXN9z0YVr9vigVIemBWDG9GhQYhWNrBTuD7Ixtqgi6JlmPeelhJA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAWfUbf12zxqatRKwy5Kf2IQ8pc9JsGNLlsZbY_hQSmk2_uQhPc3H6kWI2s5KRR4mp6RT0kWtCuByZ5g3RNDFpXalYP6CAYpoYiM-JDTd6W8nva43Q6OVfPnfikkRXnel5EhB4NJByDh7uBopTzzi5zbGfGhTSJsMfw8qT-os5_B3xuta8KGUv7Q&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA8-iHxSnkTcj0F5BkdKM5keQkL5cH8J13sAGG89f8U5McEOxJ8bZs31JW7kWMLCcJU2DnXlxSHqXChnqp4LX0L5k-TVOA-HQCjqqkA_cbxsRRPg7QIePivM_8-V1rPzMPEhAKRh3EaCan9R-GPnmBmWNxGhTORi66N0ums33D5K_88zKMvwJuhQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAATPfG5uVS0EiRsHzZieIdQ6hR9EdhNSg-_OsokoSyF-L0qPFhBpQz53bi1eq9T0apEMUpylXDkbRbmBtpEWa0xe8ne7txMDYjtB3FIlA3I1WMSqy52cq_esApR1pbn6KaEhDeuDY8KWRB57iiVzhjwFooGhToQQCQepE_WRQh5QtRHUpGDJVXaA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAFfWK0Th9Eily6cH2XXAH79c8Juj2aQ58tWkI0_2XSDp5DP2xwWBWf65BMk3SI-WR-jhJIbItWXzqUS9xH7v45NdaVDbAc3rI8_591cNtkeYtLtq93Eb5wBjKcH2D6MGgEhBohMkqWZ0EIOWwy2r8ImJiGhRmHi7sp58gL84YriS8lBhNSzuQsQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAAbe3BZExuqzug8a4T29B3xqblg-KNLw9HEI7RCM6FNSrv0_ayT6cT7_BlZIzWrUalF902RkuoUrvH4EirLZoUTQyBG7L1T9N5d3mCv4LqjvVsEWVLrMMHUPd0t6gXZg0-EhCCMjz-qwPDORKWMG_5vHO_GhTkIb_mWTyol8iGh3tMAP4t_uAEtg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                ],
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
                "expected_time": 69,
                "photos": [
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAD0cza-xyw9G82PFBgKbNJ13Qv79T0oWeAheDweYedr8z8ydxRGyJn1d6_JcC2o2i6d0TXHSC7syBdzZqGxi4xeXvO1a40gIBp3uKY7bcPvd0AV7tI6fnbXH4j176QD0GEhB_96kKxqLvn9YGipd_Uv0GGhR0WqrwuCxe3fQJ-G6ZLi5D229Qdg&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAYDx7TKo3Cdqh4e9a2x2Emy8z8f1vsYhzNJBxkwbSv58pjs-Xq8TYAU60McfRYXGblxxBJISDcSdPahEhdLv6RZP1Ugo8B186pNa61MJQHiyDVwHf8HRmuFdiiUhM6SsqEhBeeoxF3YFp5wkJ3JHkEyS4GhT6HOfI9l3Bp3EUSqRPzG_UckVqiw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRZAAAACGNMczn6_fac9O7OIbnMBzUUdJbR-PRJmUvW2JWhsZNeAdVIAiMNf57NMb6Ym1LyLacv0qwu3_ZRYAOvpXnkP96hzVjkPx_8vLUeQfpLfSxWQ5S5wlQPuo4zO4TT7aBGEhAZSN7xrsDH9RhLtfOvQ_ueGhSEUHcM9UOlZRVrDogk5u82u3ifnA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAHDKmw5Jih-UwKQKann9SZDyiS-LKbpg-wIXUzhi-kgyBOioCW3UmazVOY-g37oC7FFT57AJ_Eii37LmI-9V2HLDctnPSkiv83dXJISXMO8jQiojh7OGg6yn3kHv5HyA0EhB8kdrZiw9WS3PMsa_CWmL2GhThW5B3_K0zTEr6d6kEZPZK1CmBow&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAQr3_b1CWV-hnywx2-VZdkPAUgIo_yurB7s16kax00hZULIIl6hWCLpnsbz700cf7S4AzT8yEkb1-Ym6sbDilU6ibstIqMiHWykifBPuDDouCcZUvPf4YjXnIIg0IaJEJEhBYA8M5vHe2vySPiDxFRT91GhRwphqNSOh0euhH3SrvGrfh7II2dw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA4QgWjhdB2O83bFWhvRvEMuQaBOeXvk6YKCdflXw-X3rMK0ISvGVPoacnuZvtegFwPeUpnbjVJDtghU_2rr2yd3z2AqcgRcTRLqEXTN_nap2C8xnAV8jC4pXFLmwKM_EfEhBynjuyKfp6DxpmZnNcC6N9GhTwU6er5GFV_w-uavgE02_IdHMaAw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA07AFK9n-gCjtSHvivy9Qar7mgvk2fc88Z4orwLblAcEV4hKtbkpj1Y7HDnBUZRsk9DiEgJZLcQ_iNg3WZm4Ce6m_ALzGIWLtTWxhxjdeRsoKRdLVmfnlaKGogqmyMt4SEhA_iuHkf9bN8AFCphZ0P4k7GhRHxOQhalk8l9PkMdBBXwdfjkRPVw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAkoQj42RaEr0nf8PKyHbLSdpERLamUS9JC-TLEpNw9fiow4GOkPt0UI1kbSsogFWIJXe5Lu4F3Cc0e78aalO7jTCTmWIwuNQM3rcG3F9t36cEahnOK4S1Ilz9ESTnCnapEhDNxsoFWPoPvyuN0codELe7GhS0BNdlVzaRBs6sC-a68LAOupV5sw&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAAJcAoOGFl6dT-7FRqi6MrhdMGwuWaTHcgTZjNrKL_kJ-vKvtGoX4D-b4cnRCjGLdChR4P1T8AbQBljj2E6pC5TFrscnvsLvrjXsSvG5th1spcIwKx-K6jHX4HeGBTbhZOEhDf7dEi1ur_mjrLf0oo9BO-GhTvGFoCRR3yV6Kg3jTt6xiIGHyMUQ&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
                    "https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight=300&photoreference=CmRaAAAA1jxlZYZ6taCN9b4L76yEKCUVP3i-sLTH9BfNa06o5eL_NP8bvpZl1LDfJ0tPUzGCanhH4YgxrMTu8swu_SCBGQRYYm4j-25bqCJm81323P6rlUNt420-LYhDJbIhpZkUEhDCN65GwkvG0uOkbwoLbIjvGhQ9Gmr2d9Ki5YuLQxTN6ov5BBQRsA&key=AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s",
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
                "expected_time": 32,
                "photos": [],
            },
        ],
    ]

    time_matrix = [
        [
            [
                None,
                {
                    "duration": 46.88333333333333,
                    "points": "lkb@xs_~MJG{@uAUYG@EBURGNEXGh@c@AM~@K~@c@dASCiAAeC]_C_@yDYi@WYA_@GWCO@SDGCKAW`Ci@hFOpAUbBo@`Fm@fGJJDJAJAHCBMLA?CAIt@Ir@g@|DcAnIa@jDUhBB@VJ^Jj@b@TNFDPF\\FzBRlCXUdB]zBc@pDUvAQnAi@rDOdAb@F|BZJBX`@d@^f@V\\HZCHC@\\RfDH^FNTXvAv@f@ZPFP?TCL?RHb@RNV@Bf@SPE@A?ICUBGZW\\IF@NXLC",
                },
                {
                    "duration": 43.733333333333334,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNN@HOTMnFh@xGr@bD\\r@BVEf@I\\MrAs@tEeCl@Uj@Q^GbAVt@QRON_@Rw@PUVIX?rEtAdDbAhAf@HBHQTeBFKJGLAn@HTDT?~B]NC`Ba@NB@?@ABG?Al@IX@`@Fl@LT@hCB^BdCf@nBb@lBTlCXRNpCcAxB_A~@a@AWBGJKNCJ?FDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C?ABCHAD?@@@?BER]SYGE",
                },
                {
                    "duration": 69.3,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNb@B^?pBNZN^BZKVAN@^T^C|AJdALzATf@JNFf@NN?NCTGhD\\^^JHN?LDPf@FVJRDHBCRCxB~DhCbFbA|Bn@tAj@zAfAtCfCnGnDfJhCtGn@tAXn@l@zAv@pBRl@VXp@Tb@PfB`@lBh@vEzAhDjA`EpAlCz@dC~@xDhApBv@nEzAxAh@j@TvAXr@Xl@PvA\\zATvANjAXELy@lD}@fDo@bC]hBJjEHpCLhD~@GZ@fCj@rFnAnFjA|@X@HH^T^FLAFERBHNk@PLNNTLBFFJ",
                },
                {
                    "duration": 52.28333333333333,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNb@B^?pBNZN^BZKVAN@^T^C|AJdALzATf@JNFf@NN?NCTGhD\\^^JHN?LDPf@FVJRDHBCRCxB~DhCbFbA|Bn@tAj@zAfAtChCHlEEzBBx@FnAXjBx@zAj@tB~@~Al@pAl@RPLBzAf@vBx@jBh@z@PbBb@dAZjAb@PLxApCl@xAt@xA~AnDN\\XV|EzB~C|ApCjAjE~B~BfA~BtA\\R`@JVPhAXCj@D`@Nb@T^ZR`@JP@Il@",
                },
                {
                    "duration": 65.85,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNb@B^?pBNZN^BZKVAN@^T^C|AJdALzATf@JNFf@NN?NCTGhD\\^^JHN?LDPf@FVJRDHBCRCxB~DhCbFbA|Bn@tAj@zAfAtCfCnGnDfJhCtGn@tAXn@l@zAv@pBRl@VXp@Tb@PfB`@lBh@vEzAhDjA`EpAlCz@dC~@xDhApBv@nEzAxAh@j@TvAXcB`HkDvMkBpHd@p@|BnBp@f@n@p@nAbC`@fABF^OTG@@@@B@@?NTR\\j@bBpA`DHZH~@?F",
                },
                {
                    "duration": 52.56666666666667,
                    "points": "lkb@xs_~MJG{@uAUYG@EBURGNEXGh@l@LBJ?Je@xDU~@MTUTEDFDCtBBT?PKd@Gh@IVGP@NTb@DXDl@x@DlABz@Jp@HTFCXp@jBXj@hAjCb@x@~@vBp@|ADA|Ae@HHBP[LEAC?KBOTEP?RDXz@xBjApCtB|ERf@rBpDrBzDhAxBj@v@HAN@JDJFJN@\\ALKN|AJ|AZtF`BrIvC~E~AxBv@zGvB~CbAvDrA`@PMRAF@FBFBPHAWl@wA|Co@dA[b@@D?H?FEP?@@t@TxCBhAUl@Qd@SpAM~@A\\Fn@@n@MdAW`AEL",
                },
            ],
            [
                {
                    "duration": 46.88333333333333,
                    "points": "lkb@xs_~MJG{@uAUYG@EBURGNEXGh@c@AM~@K~@c@dASCiAAeC]_C_@yDYi@WYA_@GWCO@SDGCKAW`Ci@hFOpAUbBo@`Fm@fGJJDJAJAHCBMLA?CAIt@Ir@g@|DcAnIa@jDUhBB@VJ^Jj@b@TNFDPF\\FzBRlCXUdB]zBc@pDUvAQnAi@rDOdAb@F|BZJBX`@d@^f@V\\HZCHC@\\RfDH^FNTXvAv@f@ZPFP?TCL?RHb@RNV@Bf@SPE@A?ICUBGZW\\IF@NXLC",
                },
                None,
                {
                    "duration": 64.98333333333333,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCQFY?[Ky@e@i@q@kC_@a@GFc@Ju@l@iET{A\\yBf@{DRsA`@cDd@{CpG{BtGyBrDuAnAg@^QtAc@|DuAzAe@zBs@tAc@|@Wn@Sn@Mf@MfGyBbBg@hDgAhH}BpFmBxBo@bAYtCeA|FmB~Bq@hBs@xE_BxBq@f@QdBq@JW~Ad@fCnA^Rf@Tb@m@|BcDhAeBNOVQr@aAVSn@a@pCcAxB_A~@a@AMBQJKNCRDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C@CDAHAB@@?BER]SYGE",
                },
                {
                    "duration": 65.41666666666667,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCtBuANG~A]\\IVOZ_@Zg@N_@^_BN{@BQ`@B~APfD`@`DZtBTlALBATm@^s@|@}Bj@mBDS|BZ`Hx@dB\\VTVDRCHELK|AJ|AZtF`BrIvC~E~AxBv@zGvB~CbAvDrA`Bx@d@RdBd@~Bf@|@JV?d@HjCf@`E`AjDr@hDx@|@Tt@Bt@EtAa@|E}AVNDJTT`@LrD|@~FzAbDz@s@vCo@dHzAVjB`@JXVl@JZC?GBGLBN@@BBADLBPLLVBJPDdDr@bDr@|@XDZ^r@@JAFAF?L@BJ_@BKDBFFLJZRHP@@",
                },
                {
                    "duration": 56.583333333333336,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCtBuANG~A]\\IVOZ_@Zg@N_@^_BN{@BQ`@B~APfD`@`DZtBTlALBATm@^s@|@}Bj@mBDS|BZ`Hx@dB\\VTVDRCHELK|AJ|AZtF`BrIvC~E~AxBv@zGvB~CbAvDrA`Bx@d@RdBd@~Bf@|@JV?d@HjCf@`E`AjDr@hDx@|@Tt@Bt@EtAa@|E}AdC_AhA]zEqB`Bo@\\[^c@fBcD|AqCr@uAVPhAXCj@D`@Nb@T^ZR`@JP@Il@",
                },
                {
                    "duration": 58.71666666666667,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCtBuANG~A]\\IVOZ_@Zg@N_@^_BN{@BQ`@B~APfD`@`DZtBTlALBATm@^s@|@}Bj@mBDS|BZ`Hx@dB\\VTVDRCHELK|AJ|AZtF`BrIvC~E~AxBv@zGvB~CbAvDrA`Bx@d@RdBd@~Bf@|@JV?d@HjCf@`E`AjDr@hDx@|@Tt@Bt@El@OTKKLQNU^IT?ND^VhAj@`CZ|Ad@|BHb@L`@V^`@^tBbBt@p@Z^f@~@b@|@^bADJt@W@@@@@@D?@?Vf@Tn@`AfC`@~@Pl@Jj@@b@",
                },
                {
                    "duration": 43.75,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCtBuANG~A]\\IVOZ_@Zg@N_@^_BN{@BQ`@B~APfD`@`DZtBTlALBATm@^s@|@}Bj@mBDS|BZ`Hx@dB\\JLgBnF|F`DjCdBELHJZ@zCx@xJjD|JhDtDrArDrAEP?PBJFJJDXATMDGBp@Dd@PzC@`@EPa@`Aa@pCA\\Fn@@n@Ed@Mt@Wx@",
                },
            ],
            [
                {
                    "duration": 43.733333333333334,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNN@HOTMnFh@xGr@bD\\r@BVEf@I\\MrAs@tEeCl@Uj@Q^GbAVt@QRON_@Rw@PUVIX?rEtAdDbAhAf@HBHQTeBFKJGLAn@HTDT?~B]NC`Ba@NB@?@ABG?Al@IX@`@Fl@LT@hCB^BdCf@nBb@lBTlCXRNpCcAxB_A~@a@AWBGJKNCJ?FDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C?ABCHAD?@@@?BER]SYGE",
                },
                {
                    "duration": 64.98333333333333,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCQFY?[Ky@e@i@q@kC_@a@GFc@Ju@l@iET{A\\yBf@{DRsA`@cDd@{CpG{BtGyBrDuAnAg@^QtAc@|DuAzAe@zBs@tAc@|@Wn@Sn@Mf@MfGyBbBg@hDgAhH}BpFmBxBo@bAYtCeA|FmB~Bq@hBs@xE_BxBq@f@QdBq@JW~Ad@fCnA^Rf@Tb@m@|BcDhAeBNOVQr@aAVSn@a@pCcAxB_A~@a@AMBQJKNCRDB@tBuAVOHED@j@l@z@bANTXDXBb@AVCXUxAwAb@_@LGFE@C@CDAHAB@@?BER]SYGE",
                },
                None,
                {
                    "duration": 51.35,
                    "points": "lcg@pb_~MLJLRGHKRCDAAE?E?GDCB?@GDMFoBjBg@`@WBc@@YCYEM@Vl@Tj@~CrHfDvHjBjE^l@bBnCrArB|CxF~@bBLNM\\[rA[xAW`@UJpAbCtAbCN\\nAvBVPf@`AnCdFj@vA|AjCb@v@|BlEs@`AMVETB\\d@x@JP{@|@g@j@m@n@MZWnBCd@Bl@FnAId@e@hCQLi@BMDkAUMZcCvJeB~Hm@nCbDr@o@tCABbDr@|@X@HH^T^FLAFERBHNk@PLNNTLBFFJ",
                },
                {
                    "duration": 32.35,
                    "points": "lcg@pb_~MLJLRGHKRCDAAE?E?GDCB?@GDMFoBjBg@`@WBc@@YCYEM@Vl@Tj@~CrHfDvHjBjE^l@bBnCrArB|CxF~@bBLNM\\[rA[xAW`@UJpAbCtAbCN\\nAvBBTHLjC`F@HCNg@r@ELBHc@f@o@p@aCrCa@j@R\\Wd@Sf@o@dBc@x@[h@GRVPhAXCj@D`@Nb@T^ZR`@JP@Il@",
                },
                {
                    "duration": 51.3,
                    "points": "lcg@pb_~MLJLRGHKRCDAAE?E?GDCB?@GDMFoBjBg@`@WBc@@YCYEM@Vl@Tj@~CrHfDvHjBjE^l@bBnCrArB|CxF~@bBLNM\\[rA[xAW`@UJpAbCtAbCN\\nAvBBTHLjC`F@HCNg@r@ELBHc@f@o@p@aCrCSTTXg@~@Sf@o@dBc@x@[h@GRs@tA}ApCgBbD_@b@]ZaBn@{@ZCRe@lBmA~Es@|Bq@pCSv@JbCH`A?`A_@fEnAbC`@fABF^OTG@@@@B@@?NTR\\j@bBpA`DHZH~@?F",
                },
                {
                    "duration": 45.11666666666667,
                    "points": "lcg@pb_~MLJLRGHKRCDAAE?E?GDCB?@GDMFoBjBg@`@WBc@@YCYEFLVh@mAj@SLAH?LJVzAdDkATBDBRCNQPODOAICAAECELUr@Y`AyApEqAfEcBpFu@jC{@hCWfA_AfC{@tCsAdEy@fCyA|EuA`E}AhFeA~CMZk@dBg@nAgEzI{A`DOb@QG{@RWl@wA|Co@dA[b@@D?HANCJ@t@Dd@PzC@`@EPa@`Aa@pCA\\Fn@@n@Ed@Mt@Wx@",
                },
            ],
            [
                {
                    "duration": 69.3,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNb@B^?pBNZN^BZKVAN@^T^C|AJdALzATf@JNFf@NN?NCTGhD\\^^JHN?LDPf@FVJRDHBCRCxB~DhCbFbA|Bn@tAj@zAfAtCfCnGnDfJhCtGn@tAXn@l@zAv@pBRl@VXp@Tb@PfB`@lBh@vEzAhDjA`EpAlCz@dC~@xDhApBv@nEzAxAh@j@TvAXr@Xl@PvA\\zATvANjAXELy@lD}@fDo@bC]hBJjEHpCLhD~@GZ@fCj@rFnAnFjA|@X@HH^T^FLAFERBHNk@PLNNTLBFFJ",
                },
                {
                    "duration": 65.41666666666667,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCtBuANG~A]\\IVOZ_@Zg@N_@^_BN{@BQ`@B~APfD`@`DZtBTlALBATm@^s@|@}Bj@mBDS|BZ`Hx@dB\\VTVDRCHELK|AJ|AZtF`BrIvC~E~AxBv@zGvB~CbAvDrA`Bx@d@RdBd@~Bf@|@JV?d@HjCf@`E`AjDr@hDx@|@Tt@Bt@EtAa@|E}AVNDJTT`@LrD|@~FzAbDz@s@vCo@dHzAVjB`@JXVl@JZC?GBGLBN@@BBADLBPLLVBJPDdDr@bDr@|@XDZ^r@@JAFAF?L@BJ_@BKDBFFLJZRHP@@",
                },
                {
                    "duration": 51.35,
                    "points": "lcg@pb_~MLJLRGHKRCDAAE?E?GDCB?@GDMFoBjBg@`@WBc@@YCYEM@Vl@Tj@~CrHfDvHjBjE^l@bBnCrArB|CxF~@bBLNM\\[rA[xAW`@UJpAbCtAbCN\\nAvBVPf@`AnCdFj@vA|AjCb@v@|BlEs@`AMVETB\\d@x@JP{@|@g@j@m@n@MZWnBCd@Bl@FnAId@e@hCQLi@BMDkAUMZcCvJeB~Hm@nCbDr@o@tCABbDr@|@X@HH^T^FLAFERBHNk@PLNNTLBFFJ",
                },
                None,
                {
                    "duration": 16.65,
                    "points": "`dh@nld~MGKCGUMOOGGIEOj@CI@IDS]k@I_@AI}@YcDs@@C|AeHcDs@ViAp@_DnBaIr@uCHQ_D}@_@KFUw@Wb@wELkA",
                },
                {
                    "duration": 13.183333333333334,
                    "points": "`dh@nld~MJT?j@?VD@BDKBEHCNCbAETCA}@MeBi@eBa@gB]{@QSz@u@|CSn@E?QCiCm@]`Be@EOAiAHUBQC?QBY?CWACAAE?Y",
                },
                {
                    "duration": 39.0,
                    "points": "`dh@nld~MJT?j@?VD@BDKBEHCNCbAETCA}@MeBi@eBa@gB]{@QSz@u@|CSn@E?QCiCm@]`Be@EOAiAHUBYXANANCLMRMDQAOCh@xABLCHKNIFq@CuEUeAK}A@gA?aALaI|A]Hk@XqB`@yAZ_AHc@AuBOoFW~@kF?gDSuCMg@w@iAo@}@Ka@?aA?yBaDe@cDg@}AY_Dk@_@IEL",
                },
            ],
            [
                {
                    "duration": 52.28333333333333,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNb@B^?pBNZN^BZKVAN@^T^C|AJdALzATf@JNFf@NN?NCTGhD\\^^JHN?LDPf@FVJRDHBCRCxB~DhCbFbA|Bn@tAj@zAfAtChCHlEEzBBx@FnAXjBx@zAj@tB~@~Al@pAl@RPLBzAf@vBx@jBh@z@PbBb@dAZjAb@PLxApCl@xAt@xA~AnDN\\XV|EzB~C|ApCjAjE~B~BfA~BtA\\R`@JVPhAXCj@D`@Nb@T^ZR`@JP@Il@",
                },
                {
                    "duration": 56.583333333333336,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCtBuANG~A]\\IVOZ_@Zg@N_@^_BN{@BQ`@B~APfD`@`DZtBTlALBATm@^s@|@}Bj@mBDS|BZ`Hx@dB\\VTVDRCHELK|AJ|AZtF`BrIvC~E~AxBv@zGvB~CbAvDrA`Bx@d@RdBd@~Bf@|@JV?d@HjCf@`E`AjDr@hDx@|@Tt@Bt@EtAa@|E}AdC_AhA]zEqB`Bo@\\[^c@fBcD|AqCr@uAVPhAXCj@D`@Nb@T^ZR`@JP@Il@",
                },
                {
                    "duration": 32.35,
                    "points": "lcg@pb_~MLJLRGHKRCDAAE?E?GDCB?@GDMFoBjBg@`@WBc@@YCYEM@Vl@Tj@~CrHfDvHjBjE^l@bBnCrArB|CxF~@bBLNM\\[rA[xAW`@UJpAbCtAbCN\\nAvBBTHLjC`F@HCNg@r@ELBHc@f@o@p@aCrCa@j@R\\Wd@Sf@o@dBc@x@[h@GRVPhAXCj@D`@Nb@T^ZR`@JP@Il@",
                },
                {
                    "duration": 16.65,
                    "points": "`dh@nld~MGKCGUMOOGGIEOj@CI@IDS]k@I_@AI}@YcDs@@C|AeHcDs@ViAp@_DnBaIr@uCHQ_D}@_@KFUw@Wb@wELkA",
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
            ],
            [
                {
                    "duration": 65.85,
                    "points": "lkb@xs_~MJG{@uAUYJ?V?fAHx@A`AJt@Z|El@h@IRCdAJZNb@B^?pBNZN^BZKVAN@^T^C|AJdALzATf@JNFf@NN?NCTGhD\\^^JHN?LDPf@FVJRDHBCRCxB~DhCbFbA|Bn@tAj@zAfAtCfCnGnDfJhCtGn@tAXn@l@zAv@pBRl@VXp@Tb@PfB`@lBh@vEzAhDjA`EpAlCz@dC~@xDhApBv@nEzAxAh@j@TvAXcB`HkDvMkBpHd@p@|BnBp@f@n@p@nAbC`@fABF^OTG@@@@B@@?NTR\\j@bBpA`DHZH~@?F",
                },
                {
                    "duration": 58.71666666666667,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCtBuANG~A]\\IVOZ_@Zg@N_@^_BN{@BQ`@B~APfD`@`DZtBTlALBATm@^s@|@}Bj@mBDS|BZ`Hx@dB\\VTVDRCHELK|AJ|AZtF`BrIvC~E~AxBv@zGvB~CbAvDrA`Bx@d@RdBd@~Bf@|@JV?d@HjCf@`E`AjDr@hDx@|@Tt@Bt@El@OTKKLQNU^IT?ND^VhAj@`CZ|Ad@|BHb@L`@V^`@^tBbBt@p@Z^f@~@b@|@^bADJt@W@@@@@@D?@?Vf@Tn@`AfC`@~@Pl@Jj@@b@",
                },
                {
                    "duration": 51.3,
                    "points": "lcg@pb_~MLJLRGHKRCDAAE?E?GDCB?@GDMFoBjBg@`@WBc@@YCYEM@Vl@Tj@~CrHfDvHjBjE^l@bBnCrArB|CxF~@bBLNM\\[rA[xAW`@UJpAbCtAbCN\\nAvBBTHLjC`F@HCNg@r@ELBHc@f@o@p@aCrCSTTXg@~@Sf@o@dBc@x@[h@GRs@tA}ApCgBbD_@b@]ZaBn@{@ZCRe@lBmA~Es@|Bq@pCSv@JbCH`A?`A_@fEnAbC`@fABF^OTG@@@@B@@?NTR\\j@bBpA`DHZH~@?F",
                },
                {
                    "duration": 13.183333333333334,
                    "points": "`dh@nld~MJT?j@?VD@BDKBEHCNCbAETCA}@MeBi@eBa@gB]{@QSz@u@|CSn@E?QCiCm@]`Be@EOAiAHUBQC?QBY?CWACAAE?Y",
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
            ],
            [
                {
                    "duration": 52.56666666666667,
                    "points": "lkb@xs_~MJG{@uAUYG@EBURGNEXGh@l@LBJ?Je@xDU~@MTUTEDFDCtBBT?PKd@Gh@IVGP@NTb@DXDl@x@DlABz@Jp@HTFCXp@jBXj@hAjCb@x@~@vBp@|ADA|Ae@HHBP[LEAC?KBOTEP?RDXz@xBjApCtB|ERf@rBpDrBzDhAxBj@v@HAN@JDJFJN@\\ALKN|AJ|AZtF`BrIvC~E~AxBv@zGvB~CbAvDrA`@PMRAF@FBFBPHAWl@wA|Co@dA[b@@D?H?FEP?@@t@TxCBhAUl@Qd@SpAM~@A\\Fn@@n@MdAW`AEL",
                },
                {
                    "duration": 43.75,
                    "points": "|cb@hac~MIBCAQYc@H]ZBZCHy@XIOOQi@UMCMBYBKCc@Si@]{@e@OOO[QuAMoCtBuANG~A]\\IVOZ_@Zg@N_@^_BN{@BQ`@B~APfD`@`DZtBTlALBATm@^s@|@}Bj@mBDS|BZ`Hx@dB\\JLgBnF|F`DjCdBELHJZ@zCx@xJjD|JhDtDrArDrAEP?PBJFJJDXATMDGBp@Dd@PzC@`@EPa@`Aa@pCA\\Fn@@n@Ed@Mt@Wx@",
                },
                {
                    "duration": 45.11666666666667,
                    "points": "lcg@pb_~MLJLRGHKRCDAAE?E?GDCB?@GDMFoBjBg@`@WBc@@YCYEFLVh@mAj@SLAH?LJVzAdDkATBDBRCNQPODOAICAAECELUr@Y`AyApEqAfEcBpFu@jC{@hCWfA_AfC{@tCsAdEy@fCyA|EuA`E}AhFeA~CMZk@dBg@nAgEzI{A`DOb@QG{@RWl@wA|Co@dA[b@@D?HANCJ@t@Dd@PzC@`@EPa@`Aa@pCA\\Fn@@n@Ed@Mt@Wx@",
                },
                {
                    "duration": 39.0,
                    "points": "`dh@nld~MJT?j@?VD@BDKBEHCNCbAETCA}@MeBi@eBa@gB]{@QSz@u@|CSn@E?QCiCm@]`Be@EOAiAHUBYXANANCLMRMDQAOCh@xABLCHKNIFq@CuEUeAK}A@gA?aALaI|A]Hk@XqB`@yAZ_AHc@AuBOoFW~@kF?gDSuCMg@w@iAo@}@Ka@?aA?yBaDe@cDg@}AY_Dk@_@IEL",
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
            ],
        ],
        [
            [
                None,
                {
                    "duration": 15.616666666666667,
                    "points": "njj@v{b~MQOyAUKAMF_@b@w@z@YZSZUZq@c@wFeDMu@I@eBZqB`@s@NQNUP}A`@QBWL]NaD|@oDjAMFFLLXl@lBlArD",
                },
                {
                    "duration": 31.05,
                    "points": "njj@v{b~MQOyAUKAMF_@b@w@z@YZSZUZq@c@wFeDMu@I@eBZqB`@s@NQNUP}A`@QBWL]NaD|@oDjAMFI]Ka@K_@Ma@O_@mB|AsBvAiDtCGFu@{@y@r@]RSDIAQGcB{@q@WcBe@kAUIPs@tCoB`I_BlHWjAKCILGDg@PMGYGUD?FEDE?GEKDCAME",
                },
                {
                    "duration": 58.983333333333334,
                    "points": "njj@v{b~MZt@b@xAF?ZPlBbARTRNTJb@RJHRd@VZJDFLDRAJAJDHBDFERMROLMFOHMRCP?HT`B~A^VNFHRXl@XNBDJLHRL?B`B?f@CtBIrGA~AG@AHNB?Rd@NLBbBEpAKv@AVBl@TlATxAXl@NR@b@GjDy@f@GZe@Pm@\\_DFYJSnA_Bh@]NIHC@BVZBA|@GnE]~@Cf@Kr@c@DC@o@Gy@UoAoDcIkDiHk@w@EEy@eAaA_AyB{BmAgBmAeCgDyEyB{CoAaBk@eA[kA@mBZqE?iAK_AUy@sA}Ce@cBKm@Cs@FmANs@Pg@|DuGjAeBvA_Cz@}@xAgAb@U",
                },
                {
                    "duration": 21.083333333333332,
                    "points": "njj@v{b~MQOyAUKAMF_@b@w@z@YZSZUZq@c@wFeDu@}EYeBa@uAw@yBL]XLXi@^e@f@]oAwBSa@IWCWA}@E_ECu@Ga@GWSY[SEgAUkCJIP]?UGAGACIGSIKKEEe@Dk@s@UeAMj@_EuDi@",
                },
                {
                    "duration": 24.583333333333332,
                    "points": "njj@v{b~MZt@b@xAF?ZPlBbARTRNTJb@RJHRd@VZJDFLDRAJAJDHBDFERMROLMFOHMRCP?HT`B~A^VNFHRXl@XNBDJLHRL?B`B?f@CtBIrGA~AG@AHNB?Rd@NLBbBEpAKv@AVBl@TlATxAXl@NR@b@GjDy@f@Ge@d@c@RsAh@sA^_@HM@K?BBFDl@Al@E~@UxBu@JE\\GAL@d@LNPNr@^",
                },
                {
                    "duration": 14.45,
                    "points": "njj@v{b~MZt@b@xAF?ZPlBbARTRNTJb@RJHRd@VZJDFLDRAJAJDHBDFERMROLMFOHMRCP?HT`B~A^VNFHRXl@XNBDJLHRV?PNfE~BlCfBHHDNHp@@vC_@FkDh@k@FMC",
                },
            ],
            [
                {
                    "duration": 15.616666666666667,
                    "points": "njj@v{b~MQOyAUKAMF_@b@w@z@YZSZUZq@c@wFeDMu@I@eBZqB`@s@NQNUP}A`@QBWL]NaD|@oDjAMFFLLXl@lBlArD",
                },
                None,
                {
                    "duration": 19.016666666666666,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPWQe@_@_BgA}@vAo@`AYTi@Fu@@[DSNg@l@]n@g@lASp@c@EqB_@wFq@kBWiEi@aDq@oDw@ILGDg@PMGYGUD?FEDE?GEKDCAME",
                },
                {
                    "duration": 64.38333333333334,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPHJNJPNHPdA`A|@v@RXJNNf@Hf@XBjChBv@l@v@l@VP|@kAFG`CbB~AxAXPr@PfCh@rAFp@E`@Qh@_@h@SxA]j@[j@o@LS\\a@r@m@f@YrAWp@E|A@pHC~BMl@JXFZFd@BBBFDJ@r@EZC\\GlBo@x@Y\\GBOHYJo@d@wEJY\\a@x@y@`@WPEvAInE]~@Cf@Kr@c@DC@o@Gy@UoAoDcIkDiHk@w@EEy@eAaA_AyB{BmAgBmAeCgDyEyB{CoAaBk@eA[kA@mBZqE?iAK_AUy@sA}Ce@cBKm@Cs@FmANs@Pg@|DuGjAeBvA_Cz@}@xAgAb@U",
                },
                {
                    "duration": 26.033333333333335,
                    "points": "bbi@|lc~MmAsDm@mBMYGMLGnDkA`D}@\\OVMDGXc@NWL_@NiABa@AaAy@kDW_Ai@yBaAiD[eAEQ^Kb@OdCw@VMPMVk@ZcAbAmDDg@Ci@EgAUkCJIP]?UGAGACIGSIKKEEe@Dk@s@UeAMj@_EuDi@",
                },
                {
                    "duration": 25.383333333333333,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPHJNJPNHPdA`A|@v@RXJNNf@Hf@XBjChBv@l@v@l@nCxBjDhCr@j@`@GfABrABJCLKt@@PCPKx@}@d@a@ZO~@QvA]VQ|@eAV[p@YlAg@d@MlHMh@Bf@THTHHj@V`@HTBV?x@SjCFr@MfA_@RG~@EZCJILSPi@d@d@l@X",
                },
                {
                    "duration": 27.383333333333333,
                    "points": "bbi@|lc~MmAsDm@mBMYGMLGnDkA`D}@vBxIHFDJXdANd@n@tA`A|A^Zb@TpJvAhANr@@l@?TBt@Fz@N~A^fARrDb@xALfBTxD^p@H`@@pCi@VnADAjAS`@ID|@yATUB_@@CA",
                },
            ],
            [
                {
                    "duration": 31.05,
                    "points": "njj@v{b~MQOyAUKAMF_@b@w@z@YZSZUZq@c@wFeDMu@I@eBZqB`@s@NQNUP}A`@QBWL]NaD|@oDjAMFI]Ka@K_@Ma@O_@mB|AsBvAiDtCGFu@{@y@r@]RSDIAQGcB{@q@WcBe@kAUIPs@tCoB`I_BlHWjAKCILGDg@PMGYGUD?FEDE?GEKDCAME",
                },
                {
                    "duration": 19.016666666666666,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPWQe@_@_BgA}@vAo@`AYTi@Fu@@[DSNg@l@]n@g@lASp@c@EqB_@wFq@kBWiEi@aDq@oDw@ILGDg@PMGYGUD?FEDE?GEKDCAME",
                },
                None,
                {
                    "duration": 75.78333333333333,
                    "points": "|og@~_d~MPFJEBBF@BABG?CJCZ@TJl@UJOnDv@`Dp@hEh@jBVvFp@pB^b@DnCvAfBfAxBtB`DhCv@l@p@h@`CpBfBwBpAaBdAqAxAgBdAsA`CbB~AxAl@X~A\\fATv@DbA?ZKx@i@pAc@p@M\\Of@c@^k@z@}@h@_@RKv@QlAKhD@dFC|AK`@Ab@FLBLDPDv@FNHr@Cp@GnA]bBm@`@IH]H]d@aFH_@NU`AeAZWVObBMpBQhCOh@Cp@YZU?kAYiBoBqEiEgJ{@wAsAcB_D}CqAaBgAsB]u@u@iAmD_FmCmDk@eAOq@KYAq@LyCPsB?i@A{@UiAwAeD_@gAWuACs@Bq@RoAPg@v@sAfDkFbAcB|@wAj@o@p@k@zA_A",
                },
                {
                    "duration": 36.93333333333333,
                    "points": "|og@~_d~MlBsIp@}C|@qDd@qBn@uCFS_@KFUGCgBi@q@uDMgAs@kEd@_AWQBKP]p@mA~@eCfAqBRYxAgB|@aAb@]VIj@?XGt@g@rAs@lC{ARKl@[V[n@w@R[z@kA~@w@`BmAd@UbAUhAO|Bi@l@GV?|ATjH~@`@LFp@JIP]?UGAGACIGSIKKEEe@Dk@s@UeAMj@_EuDi@",
                },
                {
                    "duration": 36.06666666666667,
                    "points": "|og@~_d~MPFJEBBF@BABG?CJCZ@TJl@UJOnDv@`Dp@hEh@jBVvFp@pB^b@DnCvAfBfAnBaC^OrDwAdCu@`@MLLRXJNNf@Hf@XBjChBv@l@v@l@nCxBjDhCr@j@`@GfABrABJCLKt@@PCPKx@}@d@a@ZO~@QvA]VQ|@eAV[p@YlAg@d@MlHMh@Bf@THTHHj@V`@HTBV?x@SjCFr@MfA_@RG~@EZCJILSPi@d@d@l@X",
                },
                {
                    "duration": 37.766666666666666,
                    "points": "|og@~_d~MPFJEBBF@BABG?CJCZ@TJl@UJOnDv@`Dp@hEh@jBVvFp@pB^b@DnCvAfBfAxBtB`DhCv@l@p@h@jB_CnEsFhAwA~B}Cp@_AFS`@HdAPz@NfCXh@H~Cd@hD`@v@}DPeAToAlCX~Gr@`@@pCi@VnADAjAS`@ID|@yATk@FMC",
                },
            ],
            [
                {
                    "duration": 58.983333333333334,
                    "points": "njj@v{b~MZt@b@xAF?ZPlBbARTRNTJb@RJHRd@VZJDFLDRAJAJDHBDFERMROLMFOHMRCP?HT`B~A^VNFHRXl@XNBDJLHRL?B`B?f@CtBIrGA~AG@AHNB?Rd@NLBbBEpAKv@AVBl@TlATxAXl@NR@b@GjDy@f@GZe@Pm@\\_DFYJSnA_Bh@]NIHC@BVZBA|@GnE]~@Cf@Kr@c@DC@o@Gy@UoAoDcIkDiHk@w@EEy@eAaA_AyB{BmAgBmAeCgDyEyB{CoAaBk@eA[kA@mBZqE?iAK_AUy@sA}Ce@cBKm@Cs@FmANs@Pg@|DuGjAeBvA_Cz@}@xAgAb@U",
                },
                {
                    "duration": 64.38333333333334,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPHJNJPNHPdA`A|@v@RXJNNf@Hf@XBjChBv@l@v@l@VP|@kAFG`CbB~AxAXPr@PfCh@rAFp@E`@Qh@_@h@SxA]j@[j@o@LS\\a@r@m@f@YrAWp@E|A@pHC~BMl@JXFZFd@BBBFDJ@r@EZC\\GlBo@x@Y\\GBOHYJo@d@wEJY\\a@x@y@`@WPEvAInE]~@Cf@Kr@c@DC@o@Gy@UoAoDcIkDiHk@w@EEy@eAaA_AyB{BmAgBmAeCgDyEyB{CoAaBk@eA[kA@mBZqE?iAK_AUy@sA}Ce@cBKm@Cs@FmANs@Pg@|DuGjAeBvA_Cz@}@xAgAb@U",
                },
                {
                    "duration": 75.78333333333333,
                    "points": "|og@~_d~MPFJEBBF@BABG?CJCZ@TJl@UJOnDv@`Dp@hEh@jBVvFp@pB^b@DnCvAfBfAxBtB`DhCv@l@p@h@`CpBfBwBpAaBdAqAxAgBdAsA`CbB~AxAl@X~A\\fATv@DbA?ZKx@i@pAc@p@M\\Of@c@^k@z@}@h@_@RKv@QlAKhD@dFC|AK`@Ab@FLBLDPDv@FNHr@Cp@GnA]bBm@`@IH]H]d@aFH_@NU`AeAZWVObBMpBQhCOh@Cp@YZU?kAYiBoBqEiEgJ{@wAsAcB_D}CqAaBgAsB]u@u@iAmD_FmCmDk@eAOq@KYAq@LyCPsB?i@A{@UiAwAeD_@gAWuACs@Bq@RoAPg@v@sAfDkFbAcB|@wAj@o@p@k@zA_A",
                },
                None,
                {
                    "duration": 79.8,
                    "points": "zxk@lb`~M{A~@q@j@k@n@}@vAcAbBgDjFw@rAQf@SnACp@Br@VtA^fAvAdDThA@z@?h@QrBMxC@p@JXNp@j@dAlClDlD~Et@hA\\t@fArBpA`B~C|CrAbBz@vAhEfJnBpEXhB?jA[Tq@Xi@BiCNqBP_AHY_@e@T[RUVcAtAGNGl@YbCIZQ`@QTWBm@LaDt@c@?_Ba@yB]]OUGyA@_BJgA@m@Q?SMAAI@CF??M@m@@gAHmG@oBCqBM?CKKMIM]U[u@GKWIo@g@iAoAEME?S?MDKRYZg@\\IWMD]KO?_BHk@EeAc@_@QmBkAmBw@mAo@qBiAiDsByA{@Mu@M{@a@oCa@mBaAqCGQL]XLFKZk@JMh@a@FEg@{@e@w@[q@GYA]E{EEuASo@UYSKAc@Ei@Cg@O}AHCDIL]?OACMAGSIQIEECCKAQ@]BU]Ms@Og@E^kCJs@s@IaBW_@G",
                },
                {
                    "duration": 35.916666666666664,
                    "points": "zxk@lb`~M{A~@q@j@k@n@}@vAcAbBgDjFw@rAQf@SnACp@Br@VtA^fAvAdDThA@z@?h@QrBMxC@p@JXNp@j@dAlClDlD~Et@hA\\t@fArBpA`B~C|CrAbBz@vAhEfJnBpEXhB?jA[Tq@Xi@BiCNqBPcBLWN[VaAdAOTI^e@`FI\\IZ?t@d@d@l@X",
                },
                {
                    "duration": 50.1,
                    "points": "zxk@lb`~M{A~@q@j@k@n@}@vAcAbBgDjFw@rAQf@SnACp@Br@VtA^fAvAdDThA@z@?h@QrBMxC@p@JXNp@j@dAlClDlD~Et@hA\\t@fArBpA`B~C|CrAbBz@vAhEfJnBpEXhB?jA[Tq@Xi@BiCNqBP_AHY_@e@T[RUVcAtAGNGl@YbCIZQ`@QTWBm@LaDt@c@?_Ba@yB]]OUGyA@_BJgA@m@Q?SMAAI@CF??M@m@@gA@{@~Be@NCVnALAdB]D|@sARMBi@DGC",
                },
            ],
            [
                {
                    "duration": 21.083333333333332,
                    "points": "njj@v{b~MQOyAUKAMF_@b@w@z@YZSZUZq@c@wFeDu@}EYeBa@uAw@yBL]XLXi@^e@f@]oAwBSa@IWCWA}@E_ECu@Ga@GWSY[SEgAUkCJIP]?UGAGACIGSIKKEEe@Dk@s@UeAMj@_EuDi@",
                },
                {
                    "duration": 26.033333333333335,
                    "points": "bbi@|lc~MmAsDm@mBMYGMLGnDkA`D}@\\OVMDGXc@NWL_@NiABa@AaAy@kDW_Ai@yBaAiD[eAEQ^Kb@OdCw@VMPMVk@ZcAbAmDDg@Ci@EgAUkCJIP]?UGAGACIGSIKKEEe@Dk@s@UeAMj@_EuDi@",
                },
                {
                    "duration": 36.93333333333333,
                    "points": "|og@~_d~MlBsIp@}C|@qDd@qBn@uCFS_@KFUGCgBi@q@uDMgAs@kEd@_AWQBKP]p@mA~@eCfAqBRYxAgB|@aAb@]VIj@?XGt@g@rAs@lC{ARKl@[V[n@w@R[z@kA~@w@`BmAd@UbAUhAO|Bi@l@GV?|ATjH~@`@LFp@JIP]?UGAGACIGSIKKEEe@Dk@s@UeAMj@_EuDi@",
                },
                {
                    "duration": 79.8,
                    "points": "zxk@lb`~M{A~@q@j@k@n@}@vAcAbBgDjFw@rAQf@SnACp@Br@VtA^fAvAdDThA@z@?h@QrBMxC@p@JXNp@j@dAlClDlD~Et@hA\\t@fArBpA`B~C|CrAbBz@vAhEfJnBpEXhB?jA[Tq@Xi@BiCNqBP_AHY_@e@T[RUVcAtAGNGl@YbCIZQ`@QTWBm@LaDt@c@?_Ba@yB]]OUGyA@_BJgA@m@Q?SMAAI@CF??M@m@@gAHmG@oBCqBM?CKKMIM]U[u@GKWIo@g@iAoAEME?S?MDKRYZg@\\IWMD]KO?_BHk@EeAc@_@QmBkAmBw@mAo@qBiAiDsByA{@Mu@M{@a@oCa@mBaAqCGQL]XLFKZk@JMh@a@FEg@{@e@w@[q@GYA]E{EEuASo@UYSKAc@Ei@Cg@O}AHCDIL]?OACMAGSIQIEECCKAQ@]BU]Ms@Og@E^kCJs@s@IaBW_@G",
                },
                None,
                {
                    "duration": 47.78333333333333,
                    "points": "pgi@b}`~MtDh@k@~DdALr@TEj@Dd@JDHJJ`@DTPZx@~ApAhCb@z@Xn@n@nBZr@b@p@|AtAt@^hCl@f@FdBPzAVv@Tz@f@|AdAlAl@l@VxA|@|@d@jAf@vBjAlAz@h@v@j@bA`@jA^hAd@|@SHZZrAxAb@b@n@Zl@NfEt@hAN|@\\NHVTX`@\\r@jAlA|@r@f@Xt@b@rA`@fBhATV\\j@Jd@@ZCp@Q~@Ov@a@jAYfAI`@IjA?b@BjHBtA@PH\\b@v@ZTFLTZDRFr@?RGLQXQBuAPuAVYHe@D_@JU@o@HE??GCSUIMQK[?UPaAFu@?S?WFMBQZgBP{A@g@Ie@Sa@YU",
                },
                {
                    "duration": 39.06666666666667,
                    "points": "pgi@b}`~MtDh@k@~DdALr@TEj@Dd@JDHJFRBHF@D?@@AVOZKHTjCDfAZRRXFVF`@Bt@D~D@|@BVHVR`@nAvBg@\\_@d@Yh@YMM\\`@fATp@`@tAXdBt@|EvFdDp@b@vBlAhCdArAz@v@`@`Ab@TFP@j@Ap@EZA^JLABC?FDHBDFERM`@]LWHI^?HT`B~A^VNFZt@FJXNBDJLHRV?PNfE~BlCfBHHDNHp@@vCqBZoBX_@@CA",
                },
            ],
            [
                {
                    "duration": 24.583333333333332,
                    "points": "njj@v{b~MZt@b@xAF?ZPlBbARTRNTJb@RJHRd@VZJDFLDRAJAJDHBDFERMROLMFOHMRCP?HT`B~A^VNFHRXl@XNBDJLHRL?B`B?f@CtBIrGA~AG@AHNB?Rd@NLBbBEpAKv@AVBl@TlATxAXl@NR@b@GjDy@f@Ge@d@c@RsAh@sA^_@HM@K?BBFDl@Al@E~@UxBu@JE\\GAL@d@LNPNr@^",
                },
                {
                    "duration": 25.383333333333333,
                    "points": "bbi@|lc~MpCbJPbA?R?`@H^BPHJNJPNHPdA`A|@v@RXJNNf@Hf@XBjChBv@l@v@l@nCxBjDhCr@j@`@GfABrABJCLKt@@PCPKx@}@d@a@ZO~@QvA]VQ|@eAV[p@YlAg@d@MlHMh@Bf@THTHHj@V`@HTBV?x@SjCFr@MfA_@RG~@EZCJILSPi@d@d@l@X",
                },
                {
                    "duration": 36.06666666666667,
                    "points": "|og@~_d~MPFJEBBF@BABG?CJCZ@TJl@UJOnDv@`Dp@hEh@jBVvFp@pB^b@DnCvAfBfAnBaC^OrDwAdCu@`@MLLRXJNNf@Hf@XBjChBv@l@v@l@nCxBjDhCr@j@`@GfABrABJCLKt@@PCPKx@}@d@a@ZO~@QvA]VQ|@eAV[p@YlAg@d@MlHMh@Bf@THTHHj@V`@HTBV?x@SjCFr@MfA_@RG~@EZCJILSPi@d@d@l@X",
                },
                {
                    "duration": 35.916666666666664,
                    "points": "zxk@lb`~M{A~@q@j@k@n@}@vAcAbBgDjFw@rAQf@SnACp@Br@VtA^fAvAdDThA@z@?h@QrBMxC@p@JXNp@j@dAlClDlD~Et@hA\\t@fArBpA`B~C|CrAbBz@vAhEfJnBpEXhB?jA[Tq@Xi@BiCNqBPcBLWN[VaAdAOTI^e@`FI\\IZ?t@d@d@l@X",
                },
                {
                    "duration": 47.78333333333333,
                    "points": "pgi@b}`~MtDh@k@~DdALr@TEj@Dd@JDHJJ`@DTPZx@~ApAhCb@z@Xn@n@nBZr@b@p@|AtAt@^hCl@f@FdBPzAVv@Tz@f@|AdAlAl@l@VxA|@|@d@jAf@vBjAlAz@h@v@j@bA`@jA^hAd@|@SHZZrAxAb@b@n@Zl@NfEt@hAN|@\\NHVTX`@\\r@jAlA|@r@f@Xt@b@rA`@fBhATV\\j@Jd@@ZCp@Q~@Ov@a@jAYfAI`@IjA?b@BjHBtA@PH\\b@v@ZTFLTZDRFr@?RGLQXQBuAPuAVYHe@D_@JU@o@HE??GCSUIMQK[?UPaAFu@?S?WFMBQZgBP{A@g@Ie@Sa@YU",
                },
                None,
                {
                    "duration": 21.233333333333334,
                    "points": "j`l@pjd~Ms@_@QOMOAe@@M]FKDyBt@_ATm@Dm@@GECCJ?LA^IrA_@rAi@b@Sd@e@g@FkDx@c@FSAm@OyAYmAUm@UWCw@@qAJcBDMCe@O?SMAAA@IFA@_BB_BnCi@VnADAjAS`@ID|@yATk@FMC",
                },
            ],
            [
                {
                    "duration": 14.45,
                    "points": "njj@v{b~MZt@b@xAF?ZPlBbARTRNTJb@RJHRd@VZJDFLDRAJAJDHBDFERMROLMFOHMRCP?HT`B~A^VNFHRXl@XNBDJLHRV?PNfE~BlCfBHHDNHp@@vC_@FkDh@k@FMC",
                },
                {
                    "duration": 27.383333333333333,
                    "points": "bbi@|lc~MmAsDm@mBMYGMLGnDkA`D}@vBxIHFDJXdANd@n@tA`A|A^Zb@TpJvAhANr@@l@?TBt@Fz@N~A^fARrDb@xALfBTxD^p@H`@@pCi@VnADAjAS`@ID|@yATUB_@@CA",
                },
                {
                    "duration": 37.766666666666666,
                    "points": "|og@~_d~MPFJEBBF@BABG?CJCZ@TJl@UJOnDv@`Dp@hEh@jBVvFp@pB^b@DnCvAfBfAxBtB`DhCv@l@p@h@jB_CnEsFhAwA~B}Cp@_AFS`@HdAPz@NfCXh@H~Cd@hD`@v@}DPeAToAlCX~Gr@`@@pCi@VnADAjAS`@ID|@yATk@FMC",
                },
                {
                    "duration": 50.1,
                    "points": "zxk@lb`~M{A~@q@j@k@n@}@vAcAbBgDjFw@rAQf@SnACp@Br@VtA^fAvAdDThA@z@?h@QrBMxC@p@JXNp@j@dAlClDlD~Et@hA\\t@fArBpA`B~C|CrAbBz@vAhEfJnBpEXhB?jA[Tq@Xi@BiCNqBP_AHY_@e@T[RUVcAtAGNGl@YbCIZQ`@QTWBm@LaDt@c@?_Ba@yB]]OUGyA@_BJgA@m@Q?SMAAI@CF??M@m@@gA@{@~Be@NCVnALAdB]D|@sARMBi@DGC",
                },
                {
                    "duration": 39.06666666666667,
                    "points": "pgi@b}`~MtDh@k@~DdALr@TEj@Dd@JDHJFRBHF@D?@@AVOZKHTjCDfAZRRXFVF`@Bt@D~D@|@BVHVR`@nAvBg@\\_@d@Yh@YMM\\`@fATp@`@tAXdBt@|EvFdDp@b@vBlAhCdArAz@v@`@`Ab@TFP@j@Ap@EZA^JLABC?FDHBDFERM`@]LWHI^?HT`B~A^VNFZt@FJXNBDJLHRV?PNfE~BlCfBHHDNHp@@vCqBZoBX_@@CA",
                },
                {
                    "duration": 21.233333333333334,
                    "points": "j`l@pjd~Ms@_@QOMOAe@@M]FKDyBt@_ATm@Dm@@GECCJ?LA^IrA_@rAi@b@Sd@e@g@FkDx@c@FSAm@OyAYmAUm@UWCw@@qAJcBDMCe@O?SMAAA@IFA@_BB_BnCi@VnADAjAS`@ID|@yATk@FMC",
                },
                None,
            ],
        ],
        [
            [
                None,
                {"duration": 0.6, "points": "lfe@ru}}MTg@Ro@"},
                {
                    "duration": 75.3,
                    "points": "lfe@ru}}MGDCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Lx@Xd@KJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBIHK@OGEGAK?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@WRELALNp@",
                },
                {
                    "duration": 62.6,
                    "points": "lfe@ru}}MGDCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Lx@Xd@KJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRCLg@Iw@QERC`@@b@D`@DTaANs@F_ACeEs@eASSr@a@dBCLgBAO?a@Gs@OYAm@H?@?@ABEBA?MCqBd@_C\\U?UEo@IM@KFGJUdBIPICiAg@eA]aF{AqA_@Y?WHQTSv@O^SNu@PcAW_@Fk@Pm@TuEdCsAr@]Lg@HWDs@CcBS}Gs@iApK}Ca@Gt@",
                },
                {
                    "duration": 74.98333333333333,
                    "points": "lfe@ru}}MGDCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Lx@Xd@KJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBIHK@OGEGAK?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@kAW",
                },
                {
                    "duration": 68.28333333333333,
                    "points": "lfe@ru}}MGDCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Lx@Xd@KJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBIHK@OGEGAK?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_B`AGj@CDALU?c@@{BCaCHaDhBLAaA?E",
                },
            ],
            [
                {"duration": 0.6, "points": "lfe@ru}}MTg@Ro@"},
                None,
                {
                    "duration": 76.0,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@WRELALNp@",
                },
                {
                    "duration": 63.3,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRCLg@Iw@QERC`@@b@D`@DTaANs@F_ACeEs@eASSr@a@dBCLgBAO?a@Gs@OYAm@H?@ABCBA@A?MCqBd@_C\\U?UEo@IM@KFGJUdBIPICiAg@eA]aF{AqA_@Y?WHQTSv@O^SNu@PcAW_@Fk@Pm@TuEdCsAr@]Lg@HWDs@CcBS}Gs@iApK}Ca@Gt@",
                },
                {
                    "duration": 75.68333333333334,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@kAW",
                },
                {
                    "duration": 68.98333333333333,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_B`AGj@CDALU?c@@{BCaCHaDhBLAaA?E",
                },
            ],
            [
                {
                    "duration": 75.3,
                    "points": "lfe@ru}}MGDCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Lx@Xd@KJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBIHK@OGEGAK?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@WRELALNp@",
                },
                {
                    "duration": 76.0,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@WRELALNp@",
                },
                None,
                {
                    "duration": 26.716666666666665,
                    "points": "dtb@n}}}MVxALXRLjB\\fDb@JLHLFPMJ]VOFy@LO?_Ba@mB_@mA]UG_@^]`@QZEPCZ@p@CRVxAhArGJ~@A^Id@Yx@s@zGIt@WxB~ANxCZfCXY|BEb@~AR`Ar@L@L?NArBNZNNBT@YZy@b@sBzAb@d@JRJ`@H~@Bf@Gt@",
                },
                {
                    "duration": 1.2333333333333334,
                    "points": "dtb@n}}}M[uAW_@GC",
                },
                {
                    "duration": 19.183333333333334,
                    "points": "dtb@n}}}MOq@@M@GHKPM|B^`I~@`@@EKIMu@i@SYEO?QBOJSx@q@b@SpAe@JQdCnAdBf@bB^?VvBp@jAFhANdALPC`AGj@CLMDW@qCCaCHaDhBLAaA?E",
                },
            ],
            [
                {
                    "duration": 62.6,
                    "points": "lfe@ru}}MGDCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Lx@Xd@KJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRCLg@Iw@QERC`@@b@D`@DTaANs@F_ACeEs@eASSr@a@dBCLgBAO?a@Gs@OYAm@H?@?@ABEBA?MCqBd@_C\\U?UEo@IM@KFGJUdBIPICiAg@eA]aF{AqA_@Y?WHQTSv@O^SNu@PcAW_@Fk@Pm@TuEdCsAr@]Lg@HWDs@CcBS}Gs@iApK}Ca@Gt@",
                },
                {
                    "duration": 63.3,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRCLg@Iw@QERC`@@b@D`@DTaANs@F_ACeEs@eASSr@a@dBCLgBAO?a@Gs@OYAm@H?@ABCBA@A?MCqBd@_C\\U?UEo@IM@KFGJUdBIPICiAg@eA]aF{AqA_@Y?WHQTSv@O^SNu@PcAW_@Fk@Pm@TuEdCsAr@]Lg@HWDs@CcBS}Gs@iApK}Ca@Gt@",
                },
                {
                    "duration": 26.716666666666665,
                    "points": "dtb@n}}}MVxALXRLjB\\fDb@JLHLFPMJ]VOFy@LO?_Ba@mB_@mA]UG_@^]`@QZEPCZ@p@CRVxAhArGJ~@A^Id@Yx@s@zGIt@WxB~ANxCZfCXY|BEb@~AR`Ar@L@L?NArBNZNNBT@YZy@b@sBzAb@d@JRJ`@H~@Bf@Gt@",
                },
                None,
                {
                    "duration": 30.1,
                    "points": "nac@ja`~MFu@Cg@I_AKa@KSc@e@rB{Ax@c@X[UAOC[OsBO]@MAaAs@_BSDc@X}BgCYyC[_BOVyBHu@r@{GXy@He@@_@K_AiAsGWyABS?UA[B[DQP[\\a@^_@MGKEKAw@Ea@OwBuAiAm@nAK|@IXELKBWEMm@ST_AHc@b@JhB\\\\F",
                },
                {
                    "duration": 31.783333333333335,
                    "points": "nac@ja`~MFu@|C`@hAqKi@GHc@Hi@BUAWz@e@fBaAlCwAfAg@TMg@{@}@}AEo@Hk@HUFs@FiA?gAHyAJu@Zo@j@}@Tq@Ba@JiBL]NOb@QlCy@ZQTUBU?]SwAk@eDCWPAtAGFANU@c@?wDAkBH}BhBLAeA?A",
                },
            ],
            [
                {
                    "duration": 74.98333333333333,
                    "points": "lfe@ru}}MGDCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Lx@Xd@KJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBIHK@OGEGAK?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_BQBeAMiAOkAGwBq@?WcB_@eBg@eCoAKPSHwAh@m@b@URKRC`@N^PNl@b@HLDJa@AyFq@eEm@kAW",
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
                    "duration": 30.1,
                    "points": "nac@ja`~MFu@Cg@I_AKa@KSc@e@rB{Ax@c@X[UAOC[OsBO]@MAaAs@_BSDc@X}BgCYyC[_BOVyBHu@r@{GXy@He@@_@K_AiAsGWyABS?UA[B[DQP[\\a@^_@MGKEKAw@Ea@OwBuAiAm@nAK|@IXELKBWEMm@ST_AHc@b@JhB\\\\F",
                },
                None,
                {
                    "duration": 18.683333333333334,
                    "points": "hrb@ty}}Md@Hd@L|AVfANlCZjCZ`@@KSi@e@KESSGQAOFc@NQ\\Yd@[~Ak@FGFK|@f@fAf@v@TpCp@?VlA`@v@P|@DhALdANb@EtAGNIHU?iCAuDH}BhBLAeA?A",
                },
            ],
            [
                {
                    "duration": 68.28333333333333,
                    "points": "lfe@ru}}MGDCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Lx@Xd@KJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBIHK@OGEGAK?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_B`AGj@CDALU?c@@{BCaCHaDhBLAaA?E",
                },
                {
                    "duration": 68.98333333333333,
                    "points": "vge@zr}}Mc@lAMNCVIbA?TH`AAt@Eb@?h@Bn@BH@LEDI^BVP^FRh@\\LTRr@FFFBT?|@Rd@FTHjAj@p@VVB`@CV?ZNjBdBPNTLb@Ln@VH@XEJEJCFC`@F|@Tb@Hf@P\\B\\BFBBHATDRLH\\F`Bf@b@Db@Dj@H@HSFqAR?FPDf@?\\FdAP`@Fb@DbDjAALCBe@CSAoFBa@H_B|@sAp@e@ZQRI^_BYgCo@gCo@gAYqCc@gA[]I[`AKNULKB_@C}Dw@qAc@mEyBe@bASBcAKq@OgBa@w@WMMOk@]oBEDIBK?MICI?E?C]X_Ah@c@P{@`@e@AOIa@i@m@sA_@c@SOQI?KF]VQ^M`@MLSD[I_@WSOES@_@Ns@t@_@Ti@Fq@EOC@Y?aAAUC_@IEIKVONKHKBK?WAYi@kDW_B`AGj@CDALU?c@@{BCaCHaDhBLAaA?E",
                },
                {
                    "duration": 19.183333333333334,
                    "points": "dtb@n}}}MOq@@M@GHKPM|B^`I~@`@@EKIMu@i@SYEO?QBOJSx@q@b@SpAe@JQdCnAdBf@bB^?VvBp@jAFhANdALPC`AGj@CLMDW@qCCaCHaDhBLAaA?E",
                },
                {
                    "duration": 31.783333333333335,
                    "points": "nac@ja`~MFu@|C`@hAqKi@GHc@Hi@BUAWz@e@fBaAlCwAfAg@TMg@{@}@}AEo@Hk@HUFs@FiA?gAHyAJu@Zo@j@}@Tq@Ba@JiBL]NOb@QlCy@ZQTUBU?]SwAk@eDCWPAtAGFANU@c@?wDAkBH}BhBLAeA?A",
                },
                {
                    "duration": 18.683333333333334,
                    "points": "hrb@ty}}Md@Hd@L|AVfANlCZjCZ`@@KSi@e@KESSGQAOFc@NQ\\Yd@[~Ak@FGFK|@f@fAf@v@TpCp@?VlA`@v@P|@DhALdANb@EtAGNIHU?iCAuDH}BhBLAeA?A",
                },
                None,
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
