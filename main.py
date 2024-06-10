from views.app import App


def main() -> None:
    gui: App = App()
    gui.mainloop()


if __name__ == "__main__":
    main()
