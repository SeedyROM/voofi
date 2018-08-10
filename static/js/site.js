$(document).ready(() => {
    const $likeButton = $('.like-button')

    const setButtonType = ($el, pk, likes) => {
        $el.html('')

        const $button = $('<button />')
        const $form = $('<form />')
        const csrf = $el.attr('data-csrf')

        if(likes) {
            $button.text('💔 Unlike')
        } else {
            $button.text('💖 Like')
        }

        $form.on('submit', (event) => {
            let url = (likes) ? '/posts/unlike/' : '/posts/like/'
            url += pk

            event.preventDefault()
            $.post({
                url: url,
                data: {
                    csrfmiddlewaretoken: csrf
                }
            })
            .done(() => {
                setButtonType($el, pk, !likes)
            })
        })

        $form.append($button)
        $el.append($form)
    }

    $likeButton.each((index, button) => {
        const $button = $(button)
        const pk = $button.attr('data-pk')

        $.get('/posts/likes/' + pk)
        .done((data) => {
            if(data.success) setButtonType($button, pk, true)
            else setButtonType($button, pk, false)
        })
    })
})