import customtkinter
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Set up the icon
icon_path = resource_path("HSR_Kafka_Icon.ico")


def center_window(main_window):
    window_width = 1000
    window_height = 500
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    main_window.geometry(f"{window_width}x{window_height}+{x}+{y}")


class mainUI:
    def setupUI(self, main_window):
        main_window.title("HSR Warp Calculator")
        main_window.geometry("1000x500")

        try:
            main_window.iconbitmap(icon_path)
        except Exception as e:
            print(f"Warning: Could not load icon. Error: {e}")

        self.dashboard = customtkinter.CTkFrame(main_window, width=300, height=450, corner_radius=10)
        self.dashboard.place(x=10, y=10)

        self.calculation = customtkinter.CTkFrame(main_window, width=670, height=450, corner_radius=10)
        self.calculation.place(x=320, y=10)

        # Dashboard

        self.lblDirections = customtkinter.CTkLabel(self.dashboard, width=30, height=30, text="Directions",
                                                    font=("Arial", 20))
        self.lblDirections.place(x=10, y=10)

        self.lblDirectionsInstruction = customtkinter.CTkLabel(self.dashboard, width=30, height=30,
                                                               text="Input current Stellar Jades,"
                                                                    "\nNormal/Special Warp Pass,"
                                                                    "\nUndying Starlight, Oneiric Shard,"
                                                                    "\nLC/Character Banner Pity,"
                                                                    "\nand Banner/Draw Date.", font=("Arial", 18))
        self.lblDirectionsInstruction.place(x=15, y=60)

        self.lblButtonGuide = customtkinter.CTkLabel(self.dashboard, width=30, height=30, text="Button Guide",
                                                     font=("Arial", 20))
        self.lblButtonGuide.place(x=10, y=200)

        self.lblButtonGuideInstructions = customtkinter.CTkLabel(self.dashboard, width=30, height=30,
                                                                 text="Normal = Stellar Jade + Warp Pass\n"
                                                                      "Normal + US = Stellar Jade + Warp Pass +\nUndying Starlight\n"
                                                                      "Normal + OS = Stellar Jade + Warp Pass +\nOneiric Shard\n"
                                                                      "All = Stellar Jade + Warp Pass +\nUndying Starlight + Oneiric Shard\n"
                                                                      "Pity = Soft Pity - Hard Pity",
                                                                 font=("Arial", 14), anchor="w")
        self.lblButtonGuideInstructions.place(x=15, y=250)

        # Calculations

        # Stellar Jades
        self.lblStellarJades = customtkinter.CTkLabel(self.calculation, width=30, height=20, text="Stellar Jades:",
                                                      font=("Arial", 20))
        self.lblStellarJades.place(x=10, y=10)

        self.lineStellarJades = customtkinter.CTkEntry(self.calculation, width=120, height=20, font=("Arial", 15),
                                                       justify='center', placeholder_text="0")
        self.lineStellarJades.configure(validate="key",
                                        validatecommand=(self.calculation.register(self.num_only), "%P"))
        self.lineStellarJades.place(x=190, y=10)

        # Warp Pass
        self.lblWarpPass = customtkinter.CTkLabel(self.calculation, width=30, height=20, text="Warp Passes:",
                                                  font=("Arial", 20))
        self.lblWarpPass.place(x=360, y=10)

        self.lineWarpPasses = customtkinter.CTkEntry(self.calculation, width=120, height=20, font=("Arial", 15),
                                                     justify='center', placeholder_text="0")
        self.lineWarpPasses.configure(validate="key",
                                      validatecommand=(self.calculation.register(self.num_only), "%P"))
        self.lineWarpPasses.place(x=520, y=10)

        # Undying Starlight
        self.lblUndyingStarlight = customtkinter.CTkLabel(self.calculation, width=30, height=20,
                                                          text="Undying Starlight:", font=("Arial", 20))
        self.lblUndyingStarlight.place(x=10, y=70)

        self.lineUndyingStarlight = customtkinter.CTkEntry(self.calculation, width=120, height=20, font=("Arial", 15),
                                                           justify='center', placeholder_text="0")
        self.lineUndyingStarlight.configure(validate="key",
                                            validatecommand=(self.calculation.register(self.num_only), "%P"))
        self.lineUndyingStarlight.place(x=190, y=70)

        # Oneiric Shards
        self.lblOneiricShards = customtkinter.CTkLabel(self.calculation, width=30, height=20, text="Oneiric Shards:",
                                                       font=("Arial", 20))
        self.lblOneiricShards.place(x=360, y=70)

        self.lineOneiricShards = customtkinter.CTkEntry(self.calculation, width=120, height=20, font=("Arial", 15),
                                                        justify='center', placeholder_text="0")
        self.lineOneiricShards.configure(validate="key",
                                         validatecommand=(self.calculation.register(self.num_only), "%P"))
        self.lineOneiricShards.place(x=520, y=70)

        # Banner Pity
        self.lblBannerPity = customtkinter.CTkLabel(self.calculation, width=30, height=20, text="Banner Pity:",
                                                    font=("Arial", 20))
        self.lblBannerPity.place(x=10, y=130)

        self.lineBannerPity = customtkinter.CTkEntry(self.calculation, width=120, height=20, font=("Arial", 15),
                                                     justify='center', placeholder_text="0")
        self.lineBannerPity.configure(validate="key",
                                      validatecommand=(self.calculation.register(self.num_only), "%P"))
        self.lineBannerPity.place(x=190, y=130)

        # Banner Pity Output
        self.btnBannerPity = customtkinter.CTkButton(self.calculation, width=20, height=20, text="Pity",
                                                     font=("Arial", 20), command=self.pityCalc)
        self.btnBannerPity.place(x=360, y=130)

        self.txtPity = customtkinter.CTkEntry(self.calculation, width=100, height=20, font=("Arial", 20))
        self.txtPity.place(x=430, y=130)

        # Calculation Buttons

        # Normal
        self.btnNormal = customtkinter.CTkButton(self.calculation, width=20, height=20, text="Normal",
                                                 font=("Arial", 20), command=self.normalCalc)
        self.btnNormal.place(x=10, y=200)

        # Normal + US
        self.btnNormalUS = customtkinter.CTkButton(self.calculation, width=20, height=20, text="Normal + US",
                                                   font=("Arial", 20), command=self.normalUSCalc)
        self.btnNormalUS.place(x=140, y=200)

        # Normal + OS
        self.btnNormalOS = customtkinter.CTkButton(self.calculation, width=20, height=20, text="Normal + OS",
                                                   font=("Arial", 20), command=self.normalOSCalc)
        self.btnNormalOS.place(x=340, y=200)

        # All
        self.btnAll = customtkinter.CTkButton(self.calculation, width=100, height=20, text="All", font=("Arial", 20),
                                              command=self.allCalc)
        self.btnAll.place(x=540, y=200)

        # Clear
        self.btnClear = customtkinter.CTkButton(self.calculation, width=100, height=20, text="Clear All",
                                                font=("Arial", 20), command=self.clearALl)
        self.btnClear.place(x=10, y=400)

        # Output
        self.txtDraws = customtkinter.CTkEntry(self.calculation, width=200, height=20, font=("Arial", 30),
                                               justify="center", state="readonly")
        self.txtDraws.place(x=230, y=270)

    def num_only(self, line):
        return line.isdigit() or line == ""

    def getPlaceHolder(self, entry_widget, placeholder=0):
        """Retrieve integer value from entry, using placeholder if empty."""
        value = entry_widget.get()
        return int(value) if value.isdigit() else placeholder

    def pityCalc(self):
        bannerPity = self.getPlaceHolder(self.lineBannerPity, 0)

        hardPity = 90 - bannerPity
        softPity = 70 - bannerPity

        pity = f"{softPity} - {hardPity}"

        self.txtPity.delete(0, "end")
        self.txtPity.insert(0, pity)

    def normalCalc(self):
        stellar_jades = self.getPlaceHolder(self.lineStellarJades, 0)
        warp_passes = self.getPlaceHolder(self.lineWarpPasses, 0)

        self.txtDraws.configure(state="normal")

        normal_draws = (stellar_jades / 160) + warp_passes
        self.txtDraws.delete(0, "end")
        self.txtDraws.insert(0, int(normal_draws))

        self.txtDraws.configure(state="readonly")

    def normalUSCalc(self):
        stellar_jades = self.getPlaceHolder(self.lineStellarJades, 0)
        undying_starlight = self.getPlaceHolder(self.lineUndyingStarlight, 0)
        warp_passes = self.getPlaceHolder(self.lineWarpPasses, 0)

        self.txtDraws.configure(state="normal")

        normalUSDraws = (stellar_jades / 160) + (undying_starlight / 20) + warp_passes
        self.txtDraws.delete(0, "end")
        self.txtDraws.insert(0, int(normalUSDraws))

        self.txtDraws.configure(state="readonly")

    def normalOSCalc(self):
        stellar_jades = self.getPlaceHolder(self.lineStellarJades, 0)
        oneiric_shards = self.getPlaceHolder(self.lineOneiricShards, 0)
        warp_passes = self.getPlaceHolder(self.lineWarpPasses, 0)

        self.txtDraws.configure(state="normal")

        normalOSDraws = (stellar_jades / 160) + (oneiric_shards / 160) + warp_passes
        self.txtDraws.delete(0, "end")
        self.txtDraws.insert(0, int(normalOSDraws))

        self.txtDraws.configure(state="readonly")

    def allCalc(self):
        stellar_jades = self.getPlaceHolder(self.lineStellarJades, 0)
        undying_starlight = self.getPlaceHolder(self.lineUndyingStarlight, 0)
        oneiric_shards = self.getPlaceHolder(self.lineOneiricShards, 0)
        warp_passes = self.getPlaceHolder(self.lineWarpPasses, 0)

        self.txtDraws.configure(state="normal")

        allDraws = (stellar_jades / 160) + (undying_starlight / 20) + (oneiric_shards / 160) + warp_passes
        self.txtDraws.delete(0, "end")
        self.txtDraws.insert(0, int(allDraws))

        self.txtDraws.configure(state="readonly")

    def clearALl(self):
        self.lineStellarJades.delete(0, "end")
        self.lineStellarJades.configure(placeholder_text="0")

        self.lineUndyingStarlight.delete(0, "end")
        self.lineUndyingStarlight.configure(placeholder_text="0")

        self.lineOneiricShards.delete(0, "end")
        self.lineOneiricShards.configure(placeholder_text="0")

        self.lineWarpPasses.delete(0, "end")
        self.lineWarpPasses.configure(placeholder_text="0")

        self.txtDraws.configure(state="normal")
        self.txtDraws.delete(0, "end")
        self.txtDraws.configure(state="readonly")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    main_window = customtkinter.CTk()
    app = mainUI()
    center_window(main_window)
    app.setupUI(main_window)
    main_window.mainloop()
