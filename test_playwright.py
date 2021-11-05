from asyncio import run

from playwright.async_api import async_playwright


class Driver:
    async def run(self):
        async with async_playwright() as f:
            dr = await f.firefox.launch(headless=False)
            self.page = await dr.new_page()
            await self.page.goto("http://www.google.com.br")
            await self.main()
            await dr.close()

    async def main(self):
        await self.click("//html/body/div[1]/div[1]/div/div/div/div[2]/a")
        await self.fill("input[type='email']", "plustijuris@gmail.com")
        await self.click("span:text('Próxima')")
        await self.fill("input[type='password']", "editora@123")
        await self.click("span:text('Próxima')")
        text = await self.content_text("a[class='NKcBbd']")
        print(text)

    async def click(self, xpath):
        await self.page.click(xpath)

    async def fill(self, xpath, text):
        await self.page.fill(xpath, text)

    async def check(self, xpath):
        return await self.page.check(xpath)

    async def type(self, xpath, text):
        await self.page.type(xpath, text)

    async def press(self, xpath, key):
        await self.page.press(xpath, key)

    async def content_text(self, xpath):
        return await self.page.text_content(xpath)


d = Driver()
run(d.run())
