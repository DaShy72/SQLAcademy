
        function checkScreenWidth1() {
            const element = document.getElementById('dynamic-element');
            if (window.innerWidth < 1000) {
                element.classList.add('d-none');
                element.classList.remove('d-block');
            } else {
                element.classList.remove('d-none');
                element.classList.add('d-block');
            }
        }

        checkScreenWidth1();
        window.addEventListener('resize', checkScreenWidth1);

        function checkScreenWidth2() {
            const element = document.getElementById('dynamic-element1');
            if (window.innerWidth < 1000) {
                element.classList.add('d-none');
                element.classList.remove('d-block');
            } else {
                element.classList.remove('d-none');
                element.classList.add('d-block');
            }
        }

        checkScreenWidth2();
        window.addEventListener('resize', checkScreenWidth2);

        function checkScreenWidth3() {
            const element = document.getElementById('dynamic-element2');
            if (window.innerWidth < 1000) {
                element.classList.add('d-none');
                element.classList.remove('d-block');
            } else {
                element.classList.remove('d-none');
                element.classList.add('d-block');
            }
        }

        checkScreenWidth3();
        window.addEventListener('resize', checkScreenWidth3);

        function checkScreenWidth() {
            const element = document.getElementById('dynamic-element3');
            if (window.innerWidth < 1000) {
                element.classList.add('d-none');
                element.classList.remove('d-block');
            } else {
                element.classList.remove('d-none');
                element.classList.add('d-block');
            }
        }

        checkScreenWidth();
        window.addEventListener('resize', checkScreenWidth);