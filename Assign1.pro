SET_PLOT, 'PS'  ;Postscript Device Output
DEVICE, /ENCAPSULATED         ;Use EPS Format
n = 129
k = 5.*FINDGEN(n) / (n-1.)    ; Coordinates
omega = SQRT(1 + k*k)         ; Dimensionless Formula
PLOT, k, omega, /ISOTROPIC, XTITLE='!8k!X', YTITLE='!7x!X', XRANGE=[0,5], YRANGE=[0,5], /XSTYLE, /YSTYLE, XTICKS=1, XMINOR=1, XTICKNAME=[' ', ' '], YTICKS=1, YMINOR=1, YTICKNAME=[' ', ' ']
OPLOT, k, k, LINESTYLE=1      ; Light Curve
OPLOT, k, REPLICATE(1, N_ELEMENTS(k)), LINESTYLE=2    ; Cut-off Frequency
XYOUTS, 0, 1, '!7x!I!8p!X', ALIGNMENT=1.2
XYOUTS, 2.5, 2.5, '!7x!6 = !8k c!X', ALIGNMENT=-0.2
DEVICE, /CLOSE
END
