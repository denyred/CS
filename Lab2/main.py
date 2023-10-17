import matplotlib.pyplot as plt


def analyze_frequency(text):
    # Removing non-letter characters
    filtered_text = ''.join(filter(str.isalpha, text)).upper()
    total_characters = len(filtered_text)

    # Creating a dictionary of frequencies
    frequencies = {char: 0 for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for char in filtered_text:
        if char in frequencies:
            frequencies[char] += 1

    # Convert counts to percentages
    for char, count in frequencies.items():
        frequencies[char] = (count / total_characters) * 100

    return frequencies


encrypted_message = """Cixvoztg oxo pnzv jvgvwxhp rnil cni qxz, adw, avhtdpv qv rtp qtgofrxwq t htzvit, qv qvsuvo wqv hifuwnsnjxpwp rqn rviv snnlxgj cni Athng'phxuqvi pxjgtwdivp xg Pqtlvpuvtiv af ztlxgj uqnwnjituqxh vgstijvzvgwpnc wqv Vsxmtavwqtg uixgwxgj wqtw cxjdivo xg wqv rnil. Wqv Ovutiwzvgw ncHxuqvip nc wqv Ixkviatgl Stanitwnixvp hngpxpwvo nc 14 ni 15 qxjq-phqnnstgo hnssvjv jitodtwvp rqn tppxjgvo wqv xgoxkxodts svwwvip xg wqvpvVsxmtavwqtg wvywp wn ngv ni wqv nwqvi nc wrn cngwp nc wfuv tp utiw nc wqvAthngxtg pvtihq. Ctaftg jtkv wqvz wqvxi sxkxgj usdp t ptstif nc tandw$50 t zngwq. Wqv pwtcc rtp cvo tgo qndpvo xg Vgjsvovr tgo QnnkviHnwwtjvp, wqv hxuqvi stanitwnixvp wtlxgj du wqv cxipw csnni nc Vgjsvovr.Wqv fndgj rnztg rqn hnsstwvo wqv rnil nc ztgf nc wqv nwqvi pwtcczvzavip rtp Vsxmvavwq Pzxwq. Pqv qto avvg , anig Tdjdpw 26, 1892, xgQdgwxgjwng, Xgoxtgt, wqv fndgjvpw nc wqv gxgv hqxsoivg nc Enqg Z. Pzxwq,t otxifztg, atglvi, tgo hndgwf Ivudasxhtg hnzzxwwvvztg, tgo qxprxcv, Pnuqt, rqn puvssvo qvi otdjqwvi'p Hqixpwxtg gtzv rxwa tg vxgpwvto nc tg t xg wqv zxoosv avhtdpv pqv rtp gnw jnxgj wn qtkv tgfngvhtssxgj qvi hqxso "Vsxmt." Tcwvi hnzusvwxgj qxjq phqnns xg Qdgwxgjwng,Vsxmvavwq twwvgovo Rnnpwvi Hnssvjv aixvcsf adw rtp jitodtwvo cinzQxsspotsv Hnssvjv xg Zxhqxjtg rqviv pqv qto ztenivo xg Vgjsxpq. Rqxsvrnilxgj tw wqv Gvraviif Sxaitif xg Hqxhtjn, pqv rtp ivhidxwvo afCtaftg tgo avjtg rnil wqviv xg 1916.Gvxwqvi pqv gni Cixvoztg qto jxkvg tgf utiwxhdsti uivkxndp wqndjqwwn hifuwnsnjf, adw wqvf avjtg wn jvw uvipngtssf xgwvivpwvo xg wqv rnil. Xwxp fvw tgnwqvi nc wqv xingxvp nc hifuwnsnjxh qxpwnif wqtw wqv xgwvivpw nc wrncnivznpw hifuwnsnjxpwp rtp tindpvo af t ctspv onhwixgv—t onhwixgv,znivnkvi, tjtxgpw rqxhq wqvf stwvi rviv wn rtjv t sxcvwxzv atwwsv. Cni twwtasv tw wqv Ixkviatgl hnwwtjvp wqvf qvtio jtdof wtsvp nc sdpwfVsxmtavwqtg sxcv, nc wqv gnw-pn-Kxijxg Bdvvg, nc hndiwxvip' xgwixjdvp tgowqv pvhivw qxpwnixvp nc wqv jivtw gtzvp nc Vgjsxpq qxpwnif—tss thwdtssfxgktsxo ovhxuqvizvgwp nc Pqtlvpuvtiv'p ustfp wvgoxgj wn uinkv wqtwAthng qto rixwwvg wqvz, ivstwvo af wqv jvgwsv, duixjqw, adw pvsc-ovsdovornztg rqn qto "ovhxuqvivo" wqvz, Zip. Vsxmtavwq Rvssp Jtssdu. Wqvpvpwnixvp pwxiivo Cixvoztg'p oniztgw xgwvivpw; qv avjtg wn on pnzv nc wqvhifuwnsnjf, tgo xgvkxwtasf xwp udxpptgw ztjxh pvvuvo sxlv wqv cdzv ncunuuxvp xgwn qxp zxgo tgo puxixw tgo xgwnyxhtwvo qxz."Rqvg xw htzv wn wqv hifuwnsnjf," qv ivhtssvo fvtip stwvi,"pnzvwqxgj xg zv cndgo tg ndwsvw."Tg dgovipwtwvzvgw. Qv pnng cndgo qxzpvsc qvto nc wqv Ovutiwzvgw ncHxuqvip tp rvss tp wqv Ovutiwzvgw nc Jvgvwxhp tw Ixkviatgl. Wqvtwwithwxng qv cvsw cni hifuwnsnjf rtp ivxgcnihvo af wqv twwithwxng qv cvsw cnit hifuwnsnjxpw: wqv bdxhl-rxwwvo tgo puixjqwsf Zxpp Pzxwq. Xg Ztf nc 1917wqvf rviv ztiixvo tgo pwtiwvo wqv znpw ctzndp qdpatgo-tgo-rxcv wvtzxg wqv qxpwnif nc hifuwnsnjf.Tzvixht qto ovhstivo rti t zngwq avcniv, tgo Ixkvi-atgl, rqxhq qtowqv ngsf jnxgj hifuwnsnjxh hnghvig xg wqv hndgwif, avjtg jvwwxgj, ng tgxgcnizts atpxp, hifuwnjitzp cni pnsdwxng cinz ktixndp jnkvigzvgwadivtdp. Uinatasf wqv znpw xzuniwtgw rviv zvpptjvp wn tgo cinz t ixgjnc 125 Qxgodp rqn, rxwq Jviztg txo, rviv wtlxgj toktgwtjv ncVgjstgo'p uivnhhdutwxng xg Vdinuv wn pwixlv cni Xgoxtg xgovuvgovghv.Wqv xgwvihvuwp rviv jxkvg wn Cixvoztg cni pnsdwxng, tgo qv bdxhlsf pnskvowqv gdzavi hxuqvi dpvo xg htasvjitzp wn Avisxg. Wqv svwwvip nc wqvustxgwvyw tgo nc wqv lvfrnio rviv witgpcnizvo xgwn oxjxwp af zvtgp nc t4 Y 7 hqvhlviantio rxwq t gnizts tsuqtavw;
wqv lvf oxjxwp rviv wqvgtoovo wn wqnpv nc wqv ustxgwvyw wn cniz wqv hxuqviwvyw. Ngv lvf rtpSTZU. Vthq tjvgw qto qxp nrg lvf, adw Cixvoztg qto gn windasv xgpnskxgj wqvz. Gni rtp qv pwdzuvo af t pfpwvz dpdtssf ivjtiovo aftztwvdip tp wqv gv usdp dswit nc hifuwnjituqxh pvhdixwf: t annl hxuqvi.
"""
english_frequencies = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228,
    'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025,
    'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987,
    'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
    'Y': 1.974, 'Z': 0.074}

message_frequencies = analyze_frequency(encrypted_message)

# Plotting
plt.figure(figsize=(14, 5))

# English Frequencies
plt.subplot(1, 2, 1)
plt.bar(english_frequencies.keys(), english_frequencies.values(), color='blue', alpha=0.7)
plt.ylim(0, 15)
plt.title("English Frequencies")
plt.ylabel("%")
plt.xlabel("Letter")

# Message Frequencies
plt.subplot(1, 2, 2)
plt.bar(message_frequencies.keys(), message_frequencies.values(), color='red', alpha=0.7)
plt.ylim(0, 15)
plt.title("Message Frequencies")
plt.ylabel("%")
plt.xlabel("Letter")

plt.tight_layout()
plt.show()
