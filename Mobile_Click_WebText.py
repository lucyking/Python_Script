    def Mobile_Click_WebText(self, target_str):
        move_delta = 10
        self._get_appium_handle()
        screen_size=self._mobilelib.get_element_size('xpath=//android.widget.FrameLayout[1]')
        screen = screen_size.values()
        screen_width = screen[0]
        screen_length = screen[1]
        # print "\nscreen_width:", screen_width,"screen_length:", screen_length

        target = self._mobilelib.get_elements('accessibility_id='+target_str,  True)
        des_loc = target.location.values()
        des_loc_y = des_loc[0]
        des_loc_x = des_loc[1]
        # print "des_loc location x:", des_loc_x
        # print "des_loc location y:", des_loc_y

        des_size = target.size.values()
        des_size_width = des_size[0]
        des_size_height = des_size[1]
        # print "des_size width:", des_size_width
        # print "des_size height:", des_size_height

        # webview_body = self._mobilelib.get_elements('xpath=//android.webkit.WebView[1]', True)
        webview_body = self._mobilelib.get_elements('class=android.webkit.WebView', True)
        webview_body = webview_body.location.values()
        webview_x = webview_body[1]
        webview_y = webview_body[0]
        # print "\nwebview_loc:",
        # print "x=" + str(webview_x), "y=" + str(webview_y)

        start_loc_y = webview_y
        start_loc_x = des_loc_x + int(des_size_width / 2)
        # print "start loc Y:", start_loc_y
        # print "start loc X:", start_loc_x

        while (des_loc_y > 0):
            if (des_loc_y < screen_length):
                des_loc_y = des_loc_y + int(des_size_height / 2)
                # self._mobilelib.swipe(start_loc_x, des_loc_y, start_loc_x + 1, des_loc_y)
                self._mobilelib.click_a_point(start_loc_x,des_loc_y)
                break
            if (des_loc_y >= screen_length):
                self._mobilelib.swipe(start_loc_x, screen_length - 1, start_loc_x, start_loc_y, 3000)
                self._mobilelib.swipe(start_loc_x, start_loc_y, start_loc_x - 30, start_loc_y,1000)
                des_loc_y = des_loc_y - (screen_length - 1 - start_loc_y) + move_delta
        # print "des_loc_y after action:", des_loc_y
