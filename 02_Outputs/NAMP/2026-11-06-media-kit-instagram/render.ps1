# render.ps1 — Exporta las piezas del media kit a PNG con Chrome headless.
#
# Uso:
#   .\render.ps1                      # renderiza todas las piezas de la tabla
#   .\render.ps1 -File plantillas/plantilla-post.html -Out post-02-x.png
#
# Requiere Chrome instalado. Cada HTML define su tamaño en <style> (html,body),
# el parámetro -WindowSize debe coincidir. --virtual-time-budget espera a que
# carguen las fuentes (Inter empaquetada en fonts/) y los assets.
# En Linux/macOS usar render.sh (mismo listado de piezas).

param(
  [string]$File = "",
  [string]$Out = "",
  [int]$Width = 1080,
  [int]$Height = 1080
)

$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$root = $PSScriptRoot

if ($File -ne "") {
  if ($Out -eq "") { $Out = [IO.Path]::ChangeExtension($File, ".png") }
  $jobs = @(@{ html = $File; png = $Out; w = $Width; h = $Height })
} else {
  $jobs = @(
    @{ html = "post-01-lanzamiento.html";  png = "post-01-lanzamiento.png";  w = 1080; h = 1080 },
    @{ html = "post-02-servicios.html";    png = "post-02-servicios.png";    w = 1080; h = 1080 },
    @{ html = "post-03-kpp.html";          png = "post-03-kpp.png";          w = 1080; h = 1080 },
    @{ html = "avatar-instagram.html";     png = "avatar-instagram.png";     w = 1080; h = 1080 },
    @{ html = "destacadas/servicios.html"; png = "destacadas/servicios.png"; w = 1080; h = 1080 },
    @{ html = "destacadas/proyectos.html"; png = "destacadas/proyectos.png"; w = 1080; h = 1080 },
    @{ html = "destacadas/demo-kpp.html";  png = "destacadas/demo-kpp.png";  w = 1080; h = 1080 },
    @{ html = "destacadas/contacto.html";  png = "destacadas/contacto.png";  w = 1080; h = 1080 }
  )
}

foreach ($job in $jobs) {
  $src = Join-Path $root $job.html
  $dst = Join-Path $root $job.png
  $uri = ([Uri]$src).AbsoluteUri
  & $chrome --headless=new --disable-gpu --hide-scrollbars `
    --force-device-scale-factor=1 `
    --virtual-time-budget=8000 `
    --window-size="$($job.w),$($job.h)" `
    --screenshot="$dst" "$uri" | Out-Null
  if (Test-Path $dst) { Write-Host "OK  $($job.png)" } else { Write-Host "FAIL $($job.png)" }
}
