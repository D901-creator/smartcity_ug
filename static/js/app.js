document.addEventListener("DOMContentLoaded", function () {

    console.log("Smart City Uganda interface loaded.");


    /*
     * MOBILE SIDEBAR
     */

    const sidebarToggle =
        document.getElementById("sidebarToggle");

    const sidebar =
        document.getElementById("smartCitySidebar");


    if (sidebarToggle && sidebar) {

        sidebarToggle.addEventListener(
            "click",
            function () {

                sidebar.classList.toggle("show");

            }
        );

    }


    /*
     * CLOSE MOBILE SIDEBAR
     * WHEN A SIDEBAR LINK IS SELECTED
     */

    const sidebarLinks =
        document.querySelectorAll(".sidebar-link");


    sidebarLinks.forEach(function (link) {

        link.addEventListener(
            "click",
            function () {

                if (
                    window.innerWidth <= 991 &&
                    sidebar
                ) {

                    sidebar.classList.remove("show");

                }

            }
        );

    });

});