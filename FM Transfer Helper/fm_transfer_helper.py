import pandas as pd
import os


def get_latest_file(folder_path):
    # Get a list of files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("No files found in the folder.")
        return None

    # Get the full path for each file
    file_paths = [os.path.join(folder_path, f) for f in files]

    # Get the latest file based on modification time
    latest_file = max(file_paths, key=os.path.getmtime)

    return latest_file


def calculate_sweeper_keeper_support_score(squad_rawdata):
    squad_rawdata['gk_core'] = (
            (squad_rawdata['1v1'] +
             squad_rawdata['Agi'] +
             squad_rawdata['Ant'] +
             squad_rawdata['Cmd'] +
             squad_rawdata['Cnt'] +
             squad_rawdata['Kic'] +
             squad_rawdata['Ref'] +
             squad_rawdata['Pos']) * 2)
    squad_rawdata['gk_secondary'] = (
            (squad_rawdata['Acc'] +
             squad_rawdata['Aer'] +
             squad_rawdata['Cmp'] +
             squad_rawdata['Com'] +
             squad_rawdata['Dec'] +
             squad_rawdata['Fir'] +
             squad_rawdata['Han'] +
             squad_rawdata['Pas'] +
             squad_rawdata['Thr'] +
             squad_rawdata['TRO'] +
             squad_rawdata['Vis']) * 1)
    squad_rawdata['gk'] = (
                ((squad_rawdata['gk_core']) + (squad_rawdata['gk_secondary'])) / 27)
    squad_rawdata.gk = squad_rawdata.gk.round(1)

    return squad_rawdata



def calculate_central_defender_defend_score(squad_rawdata):
    squad_rawdata['cd_core'] = (
            (squad_rawdata['Hea'] +
             squad_rawdata['Mar'] +
             squad_rawdata['Tck'] +
             squad_rawdata['Pos'] +
             squad_rawdata['Jum'] +
             squad_rawdata['Str']) * 2)
    squad_rawdata['cd_secondary'] = (
            (squad_rawdata['Agg'] +
             squad_rawdata['Ant'] +
             squad_rawdata['Bra'] +
             squad_rawdata['Cmp'] +
             squad_rawdata['Cnt'] +
             squad_rawdata['Dec'] +
             squad_rawdata['Pac']) * 1)
    squad_rawdata['cd'] = (
                ((squad_rawdata['cd_core']) + (squad_rawdata['cd_secondary'])) / 19)
    squad_rawdata.cd = squad_rawdata.cd.round(1)

    return squad_rawdata


def calculate_ball_playing_defender_defend_score(squad_rawdata):
    squad_rawdata['bpd_core'] = (
            (squad_rawdata['Hea'] +
             squad_rawdata['Mar'] +
             squad_rawdata['Pas'] +
             squad_rawdata['Tck'] +
             squad_rawdata['Cmp'] +
             squad_rawdata['Pos'] +
             squad_rawdata['Jum'] +
             squad_rawdata['Str']) * 2)
    squad_rawdata['bpd_secondary'] = (
            (squad_rawdata['Fir'] +
             squad_rawdata['Agg'] +
             squad_rawdata['Ant'] +
             squad_rawdata['Bra'] +
             squad_rawdata['Cnt'] +
             squad_rawdata['Dec'] +
             squad_rawdata['Vis'] +
             squad_rawdata['Pac']) * 1)
    squad_rawdata['bpd'] = (
                ((squad_rawdata['bpd_core']) + (squad_rawdata['bpd_secondary'])) / 24)
    squad_rawdata.bpd = squad_rawdata.bpd.round(1)

    return squad_rawdata


# def calculate_full_back_attack_score(squad_rawdata):
#
#
#
def calculate_full_back_support_score(squad_rawdata):
    squad_rawdata['fbs_core'] = (
            (squad_rawdata['Mar'] +
             squad_rawdata['Tck'] +
             squad_rawdata['Ant'] +
             squad_rawdata['Cnt'] +
             squad_rawdata['Pos'] +
             squad_rawdata['Tea']) * 2)
    squad_rawdata['fbs_secondary'] = (
            (squad_rawdata['Cro'] +
             squad_rawdata['Dri'] +
             squad_rawdata['Pas'] +
             squad_rawdata['Tec'] +
             squad_rawdata['Dec'] +
             squad_rawdata['Wor'] +
             squad_rawdata['Pac'] +
             squad_rawdata['Sta']) * 1)
    squad_rawdata['fbs'] = (
                ((squad_rawdata['fbs_core']) + (squad_rawdata['fbs_secondary'])) / 20)
    squad_rawdata.fbs = squad_rawdata.fbs.round(1)

    return squad_rawdata


def calculate_deep_playmaker_defend_score(squad_rawdata):
    squad_rawdata['dpd_core'] = (
            (squad_rawdata['Fir'] +
             squad_rawdata['Pas'] +
             squad_rawdata['Cmp'] +
             squad_rawdata['Dec'] +
             squad_rawdata['Tea'] +
             squad_rawdata['Vis']) * 2)
    squad_rawdata['dpd_secondary'] = (
            (squad_rawdata['Tck'] +
             squad_rawdata['Ant'] +
             squad_rawdata['Pos'] +
             squad_rawdata['Bal']) * 1)
    squad_rawdata['dpd'] = (
                ((squad_rawdata['dpd_core']) + (squad_rawdata['dpd_secondary'])) / 16)
    squad_rawdata.dpd = squad_rawdata.dpd.round(1)

    return squad_rawdata


def calculate_segundo_volante_attack_score(squad_rawdata):
    squad_rawdata['sva_core'] = (
            (squad_rawdata['Fin'] +
             squad_rawdata['Lon'] +
             squad_rawdata['Pas'] +
             squad_rawdata['Tck'] +
             squad_rawdata['Ant'] +
             squad_rawdata['OtB'] +
             squad_rawdata['Pos'] +
             squad_rawdata['Wor'] +
             squad_rawdata['Pac'] +
             squad_rawdata['Sta']) * 2)
    squad_rawdata['sva_secondary'] = (
            (squad_rawdata['Fir'] +
             squad_rawdata['Mar'] +
             squad_rawdata['Cmp'] +
             squad_rawdata['Cnt'] +
             squad_rawdata['Dec'] +
             squad_rawdata['Acc'] +
             squad_rawdata['Bal'] +
             squad_rawdata['Str']) * 1)
    squad_rawdata['sva'] = (
                ((squad_rawdata['sva_core']) + (squad_rawdata['sva_secondary'])) / 28)
    squad_rawdata.sva = squad_rawdata.sva.round(1)

    return squad_rawdata


def calculate_winger_support_score(squad_rawdata):
    squad_rawdata['ws_core'] = (
            (squad_rawdata['Cro'] +
             squad_rawdata['Dri'] +
             squad_rawdata['Tec'] +
             squad_rawdata['Acc'] +
             squad_rawdata['Agi']) * 2)
    squad_rawdata['ws_secondary'] = (
            (squad_rawdata['Fir'] +
             squad_rawdata['Pas'] +
             squad_rawdata['OtB'] +
             squad_rawdata['Wor'] +
             squad_rawdata['Bal'] +
             squad_rawdata['Pac'] +
             squad_rawdata['Sta']) * 1)
    squad_rawdata['ws'] = (
                ((squad_rawdata['ws_core']) + (squad_rawdata['ws_secondary'])) / 16)
    squad_rawdata.ws = squad_rawdata.ws.round(1)

    return squad_rawdata


# def calculate_deep_forward_support_score(squad_rawdata):
#
#
#
# def calculate_target_man_attack_score(squad_rawdata):



# Example usage
folder_path = "fm data"
latest_file = get_latest_file(folder_path)
output_path = "fm output"

if latest_file:
    print("Latest file:", latest_file)
    with open(latest_file, 'r') as file:
        content = pd.read_html(latest_file)
        # content = file.read()
        print("File content:\n", content)


# Read HTML file exported by FM - in this case an example of an output from the squad page
# This reads as a list, not a dataframe
squad_rawdata_list = pd.read_html(latest_file, header=0, encoding="utf-8", keep_default_na=False)

# turn the list into a dataframe
squad_rawdata = squad_rawdata_list[0]

calculate_sweeper_keeper_support_score(squad_rawdata)
calculate_central_defender_defend_score(squad_rawdata)
calculate_ball_playing_defender_defend_score(squad_rawdata)
calculate_full_back_support_score(squad_rawdata)
calculate_deep_playmaker_defend_score(squad_rawdata)
calculate_segundo_volante_attack_score(squad_rawdata)
calculate_winger_support_score(squad_rawdata)


print(squad_rawdata.sort_values("sva"))


