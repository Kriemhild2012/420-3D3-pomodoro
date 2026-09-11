from views.dashboard import Dashboard

if __name__ == "__main__":
    from models.minuteur import Minuteur

    minuteur = Minuteur()
    dashboard = Dashboard(minuteur)
    dashboard.mainloop()