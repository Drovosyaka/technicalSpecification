function LoadResponse() {
fetch('/api/equipment/')
        .then(response => response.json())
        .then(dataOrder => {
            //console.log(dataOrder)
            // Заголовок аккордеона
            const dataContainer = document.getElementById('accordionOrder');
            let accordionHTML = '';
            check = 0;
            dataOrder.forEach(entry => {

                    accordionHTML += `
                        <form onsubmit="return false" type="get" action="/order" class="hide_col" style="border-bottom: 2px solid rgba(0,0,0,0.13); width: 99.4%">
                            <div class="collapsed"  type="button" data-bs-toggle="collapse"
                            data-bs-target="#Acor${entry.code}" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
                                <div class="row align-items-center">
                                    <div class="col fs-5 text-end me-xxl-5" ><p>${entry.code}</p></div>
                                    <div class="col fs-5 text-end me-xxl-5"><p>${entry.code}</p></div>
                                    <div class="col fs-5 text-end me-xxl-5"><p>${entry.code}</p></div>
                                </div>
                            </div>
                            <div id="content_acc_${entry.code}"><div id="Acor${entry.code}" class="accordion-collapse collapse"></div></div>
                        </form>
                        <style>
                            .Acor${entry.code} {
                                background-color: red;
                            }
                        </style>
                    `;
            });
            dataContainer.innerHTML = accordionHTML;
        });
}