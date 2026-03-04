
import requests

#Script to find your private servers (ones that are active) from oldest to newest

# TODO: Replace these later with environment variables and proper way to get cookie
url = "https://games.roblox.com/v1/private-servers/my-private-servers?privateServersTab=0&itemsPerPage=100000"
cookie = "RBXEventTrackerV2=CreateDate=10/09/2025 12:47:21&rbxid=1326364632&browserid=1749378274162005; GuestData=UserID=-470905659; .ROBLOSECURITY=_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEaAhADIhwKBGR1aWQSFDE3MTY5Nzg1ODUyOTE4ODI1NDM5KAM.Tbf3AOH3I7Op09sXPN5qvujI25H8P3Hl6J2o-FbbYY8wPNWx-pMhZNnzmx0qmKq3g6U4klwHAvmIKh8CaTDfIMnRr8vbFkXONf2biIxrzAXKZ6N9P--sjR8LadYEXdHWzuWdId5qVAvkXfAr3KUs9-fXZfnUi1plBrLnEk0RLNyuJ336OtL5nIi44b4BGSNqPrNYUB0DYHBz3mzy1wuTStSGq0Z7nyYK9Hot-CE1ZzPz89uczEeNikt_5r-i4BH0JCa8jcZYI1GjgraW2d-cXZddRw1p8Eb_l9FnD8T58Mf4uI9zHbFaTtHAe0N44f2R3A9fQRsvhYoXTvGAHxlUMxUo3Bvg1TbkDdw1_vasNyd7S2XPvfksZ8Q7FxmZPBsj_4ogm15dETHKnr-EweIbmgvIHYeSxS0rEx-Bq4DuetHlkhSEb5zjXtr6LUP6mP5BqUPCT750YfxKhQ45nUpjfD9XVMnoEDPVcPkfUi7KUvCc_BuzrU4mYnNIP_M77xh1wnaQhfnjY7OIJxjk69k57v74XnWgz4DJl1a0vtxUk7gujPlxeWQ-8PeJQ_BJSVItzNpHGMYZKNsQDHEp_Y1jPKe01-D1HS8N2sF8yf4VFSuPA6VjAQMDjOgYgGryI21MLKGVp5UtPkdAth2wGcElx7l84cpjzeZBGpU5IBz_bqS6J7H_Eh0My_KDECT3No9y-jdeh-OGVeEbaxgkU0M8mfC0XJjdQUdH5p_utfMgslLW8ra_zuxECOOh2coc6TLb3YT8xC1_dvH2_mGP_hpCGAhgEgB7rQJLXg0XlUlreEdVxIs7; rbxas=3487122745af3e2779672869f5f417d5582ba8733cc2b449233822a31f50fe88; RBXSource=rbx_acquisition_time=12/07/2025 17:26:21&rbx_acquisition_referrer=https://www.roblox.com/share-links?code=ff2389f7f9f68640a883ad3deb8e5297&type=Server&pid=Server&is_retargeting=false&deep_link_value=roblox%3A%2F%2Fnavigation%2Fshare_links%3Fcode%3Dff2389f7f9f68640a883ad3deb8e5297%26type%3DServer&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; ak_bmsc=33B9125511D92FAC7214E6223D3FEFE9~000000000000000000000000000000~YAAQbuQWAsp/RCabAQAApBfWUB7dqXHB6SSM1DOfdiD+w98GVa5P20S1hrqsM89MueSDI7qP833izAExkoF8uhVT2OGWPOqt2U01DQt2wjAtmB6xItHZK9Xlpx4nFBEea48jsqZlTK23x+bMaTeQsp+AefV1/1uzh134BHUxTH/C8xNDwCAqnI/+qA0aPtyZjZ+ByQ407jsseazjM8GlLkBfLLLXkOqb0y5j6+ovUI1qFFTN3Luy0t34NmGhR9PEsySl1ebM1PQS38OWt+jb5mXG0gqbc05Qo7WBTaYouQeOamD0hKXTEgE5SThXIeGuaxiltp/b+zSwciFrK295r0Am2R3zoArO+vvrNdFtDd3Bm8K4gLmlWaWiS9q+lZbwxtLEkhCu1kWr/bE=; UnifiedLoggerSession=CreatorHub%3D%7B%22sessionId%22%3A%2248004293-4dc6-4875-89f6-499e4534c0f1%22%2C%22lastActivity%22%3A1766589191074%7D; rbx-ip2=rbx-ip2; bm_sv=CC170A82B9419C78CB1DF616EC3FA739~YAAQbuQWArKCRCabAQAAVzTWUB5UBO8eeh2Mt7XAOfXnI/L+ZtmC3tJTn8VWpyqDDsQEw0dx+hY2zD4/oefaKN1DbGp7cZ8t3TVHjd1105H3BeL8tG6rIv7ByKP2LPSthmjQ9jNWVPiSaNViDh3RGYunMKbrG7m5wxXT87JQMvJcNI9T9EP80mKvPeneKFaFJb9P7DBNr0yaKKkvso7cjJ+ybM0HCbBnC6tT+T3UOiXQpZarpSt8L9ROK5l0QqAC~1"
player_name = "roryawsometv2" #Replace with your username

def requestData(pageCursor):


    response = requests.get(f"{url}&cursor={pageCursor}", headers={"Cookie": cookie})

    if response.status_code == 200:

        response_data = response.json()

        if response_data["nextPageCursor"]:
            print(response_data["nextPageCursor"])

            requestData(response_data["nextPageCursor"]) #Still need to fix the page cursor
        
        return response_data
              
   
   
#player_data = requestData(1)
#print(player_data)


def returnPrivateServers(data_dictionary):
    data = data_dictionary["data"]
    active_private_servers = []

    for value in data:  # TODO: Replace with name asker soon, and then player ID to player name for fool proof solution
        if value["active"] == True and value["ownerName"] == player_name:
            active_private_servers.append(value["universeName"])

    for privateServer in active_private_servers:
        print(f"{privateServer}\n")


returnPrivateServers(requestData(1))
