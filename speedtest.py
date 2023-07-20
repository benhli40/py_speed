import speedtest
import csv

def test():
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 10**6  # Convert to Mbps
        upload_speed = st.upload() / 10**6  # Convert to Mbps
        ping = st.results.ping
        return download_speed, upload_speed, ping
    except Exception as e:
        print("Failed to test internet speed:", str(e))
        return None, None, None

def main():
    # write to csv
    with open('file.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['download', 'upload', 'ping'])
        for i in range(3):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            if d is not None and u is not None and p is not None:
                csv_writer.writerow([d, u, p])

    # pretty write to txt file
    with open('file.txt', 'w') as f:
        for i in range(3):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            if d is not None and u is not None and p is not None:
                f.write('Test #{}\n'.format(i+1))
                f.write('Download: {:.2f} Mbps\n'.format(d))
                f.write('Upload: {:.2f} Mbps\n'.format(u))
                f.write('Ping: {}\n'.format(p))

    # simply print in the desired format if you want to use pipe-style: python script.py > file
    for i in range(3):
        print('Test #{}'.format(i+1))
        d, u, p = test()
        if d is not None and u is not None and p is not None:
            print('Download: {:.2f} Mbps'.format(d))
            print('Upload: {:.2f} Mbps'.format(u))
            print('Ping: {}'.format(p))
        print()

if __name__ == '__main__':
    main()