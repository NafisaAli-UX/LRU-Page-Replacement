def lru_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0
    usage_order = []

    print("Page    Frame           Status")
    print("-----------------------------------")

    for page in pages:
        if page in frame:
            status = "Hit"
            usage_order.remove(page)
            usage_order.append(page)
        else:
            status = "Miss"
            page_faults += 1
            if len(frame) < frame_size:
                frame.append(page)
            else:
                lru_page = usage_order.pop(0)
                frame[frame.index(lru_page)] = page
            usage_order.append(page)
        print(f"{page:<7} {frame}    {status}")

    print(f"\nTotal Page Faults: {page_faults}")
frame_size = int(input("Enter frame size: "))
pages = list(map(int, input("Enter page reference string (space separated): ").split()))

lru_page_replacement(pages, frame_size)
