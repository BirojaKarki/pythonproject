import win32com.client as wincl

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
l=[" Biroja","Dhananjya","Bijaya"," kumari","rajbansh","max","hiramani","samir","Krishma"]

for item in l:
    spk.Speak(f"Shoutout to {item}")

