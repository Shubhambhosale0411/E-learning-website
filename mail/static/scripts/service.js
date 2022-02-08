// reduce transparency of content on move over navigation
const serviceContent = document.getElementsByClassName("service_content")[0]
const navigationList = document.getElementsByClassName("navigation")

for(let nav of navigationList ){
    nav.addEventListener("mouseenter", e=>{
        const backdrop = document.createElement('div')
        backdrop.setAttribute("id","content-backdrop-black")
        backdrop.style.position = "absolute"
        backdrop.style.top = "0px"
        backdrop.style.left = "0px"
        backdrop.style.width = "100%"
        backdrop.style.height = "100%"
        backdrop.style.backgroundColor = "rgba(0,0,0,0.7)"
        serviceContent.appendChild(backdrop)
    })

    nav.addEventListener("mouseleave",e=>{
        document.getElementById("content-backdrop-black").remove()
    })
}