import wfdb
import matplotlib.pyplot as plt


# Download and read ECG record 100
record = wfdb.rdrecord("100", pn_dir="mitdb")


# Display basic information
print("Sampling frequency:", record.fs)
print("Number of samples:", record.sig_len)
print("Number of channels:", record.n_sig)
print("Signal names:", record.sig_name)


# Get the first ECG channel
ecg_signal = record.p_signal[:, 0]


# Create a time axis
time = [i / record.fs for i in range(record.sig_len)]


# Plot the ECG
plt.figure(figsize=(12, 4))

plt.plot(time, ecg_signal)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.title("MIT-BIH ECG Record 100")

plt.show()
