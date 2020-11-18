class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.pages = self.pages[:self.current+1]
        self.pages.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        if self.current-steps < 0:
            self.current = 0
        else:
            self.current = self.current-steps
        return self.pages[self.current]

    def forward(self, steps: int) -> str:
        if steps+self.current >= len(self.pages):
            self.current = len(self.pages)-1
        else:
            self.current = self.current+steps
        return self.pages[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
