class Solution:
    def reverseList(self, head):
        # Pehle prev aur curr pointer define karte hain
        prev = None
        curr = head

        # Jab tak current node None nahi ho jata, loop chalayenge
        while curr:
            next_node = curr.next  # Agla node temporarily store kar lo
            curr.next = prev       # Current node ka next ab pichle node ko point karega

            # Prev aur curr ko aage badhao
            prev = curr
            curr = next_node

        # Jab loop khatam ho jaye, prev new head hoga reversed list ka
        return prev
